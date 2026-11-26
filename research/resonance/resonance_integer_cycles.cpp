#include <algorithm>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
struct DSU { vector<int> p,sz; DSU(int n):p(n),sz(n,1){iota(p.begin(),p.end(),0);} int find(int a){return p[a]==a?a:p[a]=find(p[a]);} void join(int a,int b){a=find(a);b=find(b);if(a!=b){if(sz[a]<sz[b])swap(a,b);p[b]=a;sz[a]+=sz[b];}}};
int main(){
 const int n=8,M=n*(n-1)/2,k=n-1,bits=5,mask=(1<<bits)-1;
 uint64_t C[40][10]{};for(int a=0;a<40;a++){C[a][0]=1;for(int b=1;b<10;b++)C[a][b]=(a?C[a-1][b-1]+C[a-1][b]:0);}
 auto decode=[&](uint64_t s){vector<int>a(n);for(int i=0;i<n;i++)a[i]=(s>>(i*bits))&mask;return a;};
 auto pack=[&](const vector<int>&a){uint64_t s=0;for(int i=0;i<n;i++)s|=uint64_t(a[i])<<(i*bits);return s;};
 auto index=[&](uint64_t s){uint64_t z=0;for(int i=0;i<k;i++)z+=C[((s>>((i+1)*bits))&mask)+i][i+1];return z;};
 vector<int>w(n);for(int r=0;r<n;r++)w[r]=(n-r)*(n-r-1)/2;
 auto next=[&](uint64_t s){auto a=decode(s);for(int i=0;i<n;i++)a[i]+=w[i];sort(a.begin(),a.end());int m=a[0];for(int&x:a)x-=m;return pack(a);};
 uint64_t total=C[M+n-1][n-1],visited=0,cycles=0,mean_cycles=0;vector<uint8_t>seen(total);vector<int>comb(k);iota(comb.begin(),comb.end(),0);auto start=chrono::steady_clock::now();bool complete=false;
 while(true){vector<int>a(n);for(int i=0;i<k;i++)a[i+1]=comb[i]-i;uint64_t state=pack(a);
  if(!seen[index(state)]){vector<uint64_t>trail;while(!seen[index(state)]){seen[index(state)]=1;visited++;trail.push_back(state);state=next(state);}auto it=find(trail.begin(),trail.end(),state);
   if(it!=trail.end()){cycles++;vector<vector<int>>cyc;bool mean=false;for(;it!=trail.end();it++){auto v=decode(*it);int s=accumulate(v.begin(),v.end(),0);if(s%n==0&&count(v.begin(),v.end(),s/n)>=2)mean=true;cyc.push_back(v);}
    if(mean){mean_cycles++;int p=cyc.size();DSU dsu(p*n);for(int t=0;t<p;t++){vector<int>raw(n);for(int r=0;r<n;r++)raw[r]=cyc[t][r]+w[r];int low=*min_element(raw.begin(),raw.end());for(int r=0;r<n;r++)for(int q=0;q<n;q++)if(raw[r]-low==cyc[(t+1)%p][q])dsu.join(t*n+r,((t+1)%p)*n+q);}
     for(int t=0;t<p;t++){int s=accumulate(cyc[t].begin(),cyc[t].end(),0);if(s%n)continue;int avg=s/n;for(int r=0;r+1<n;r++)if(cyc[t][r]==avg&&cyc[t][r+1]==avg){cerr<<"mean component_size="<<dsu.sz[dsu.find(t*n+r)]/p<<" phase="<<t<<" period="<<p<<" state=";for(int v:cyc[t])cerr<<v<<",";cerr<<endl;}for(int r=0;r+1<n;r++)if(cyc[t][r]==avg&&cyc[t][r+1]==avg&&dsu.sz[dsu.find(t*n+r)]==2*p){cout<<"{\"n\":"<<n<<",\"counterexample\":true,\"phase\":"<<t<<",\"ranks\":["<<r<<","<<r+1<<"],\"period\":"<<p<<",\"cycle\":[";for(int j=0;j<p;j++){if(j)cout<<",";cout<<"[";for(int q=0;q<n;q++){if(q)cout<<",";cout<<cyc[j][q];}cout<<"]";}cout<<"]}"<<endl;return 0;}}
    }
   }
  }
  int pos=k-1;while(pos>=0&&comb[pos]==M+k-1-(k-1-pos))pos--;if(pos<0){complete=true;break;}comb[pos]++;for(int j=pos+1;j<k;j++)comb[j]=comb[j-1]+1;
  if(visited%100000==0&&chrono::duration<double>(chrono::steady_clock::now()-start).count()>30)break;
 }
 cout<<"{\"n\":"<<n<<",\"complete\":"<<(complete?"true":"false")<<",\"states\":"<<visited<<",\"expected\":"<<total<<",\"cycles\":"<<cycles<<",\"cycles_with_any_mean_tie\":"<<mean_cycles<<",\"binary_mean_counterexample\":false,\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"}"<<endl;
}
