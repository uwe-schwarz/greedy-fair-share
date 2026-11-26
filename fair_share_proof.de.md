# Greedy-Fair-Share-Folgen: exakte Periodizitätsbeweise

Deutsche Fassung. Maßgeblich ist die [englische Fassung](fair_share_proof.md).

Datum: 2026-11-26

## Ergebnis und Geltungsbereich

Für die im Video beschriebene Greedy-Regel im gliedweisen Grenzwert der
Trefferwahrscheinlichkeit gegen null liefert diese Ausarbeitung:

1. Einen vollständig nachrechenbaren Beweis für **N = 3**: kleinste Periode
   54, periodisch ab dem nullbasierten Index 47, also ab dem 48. Glied.
2. Ein allgemeines, endliches Kriterium, mit dem ein vorgeschlagener
   periodischer Rest für eine beliebige feste Spielerzahl bewiesen werden kann.
3. Exakte Zertifikate für **jede Spielerzahl von 3 bis 24**. Diese beweisen
   jeweils eine unendliche periodische Fortsetzung; sie beruhen nicht auf der
   bloßen Beobachtung vieler gleicher Blöcke.
4. Einen konkreten vorübergehenden Wiederholungsblock für N = 15, dessen
   scheinbare Periode später zwingend scheitert.

**Nicht bewiesen ist der universelle Satz für alle ganzen N > 2.** Insbesondere
ist nicht bewiesen, dass die Suche nach einem Zertifikat für jede Spielerzahl
terminiert. Die endliche Liste von 22 Fällen ersetzt diesen Schritt nicht.

Die Beweise im Folgenden werden hier aus der Konstruktionsregel hergeleitet.
Es wird kein Anspruch auf wissenschaftliche Erstveröffentlichung erhoben.
Literaturangaben dienen der Einordnung des Problems, nicht als Ersatz für
die angegebenen Beweisschritte.

## 1. Präzise Definition

Die Spieler heißen 0, ..., N−1. Der Zug mit Index t beginnt bei t = 0.
Mit a_t bezeichnen wir den dort ausgewählten Spieler. Für q = 1−p sei

\[
S_i(t,q)=\sum_{\substack{0\le s<t\\a_s=i}}q^s.
\]

Die Wahrscheinlichkeit, dass Spieler i bereits gewonnen hat, ist
p S_i(t,q). Der gemeinsame positive Faktor p beeinflusst den Vergleich nicht.
Der nächste Zug geht deshalb an den Spieler mit dem kleinsten S_i(t,q)
für q hinreichend nahe bei 1 von links. Anfangs erhalten die noch nicht
aufgetretenen Spieler ihre Nummern in der Reihenfolge ihrer ersten Züge.

Dies ist ein **gliedweiser Grenzwert**: Für jeden endlichen Abschnitt darf
die notwendige obere Schranke für p anders ausfallen. Wir behaupten nicht,
dass ein einziges festes p > 0 die gesamte unendliche Grenzfolge erzeugt.

### Altersmomente

Setze

\[
q=\frac1{1+z},\qquad z>0.
\]

Multiplikation aller Spielerwerte mit dem gemeinsamen positiven Faktor
q^(−t) erhält ihre Ordnung. Damit erhalten wir

\[
G_i(t,z)=q^{-t}S_i(t,q)
=\sum_{\substack{s<t\\a_s=i}}(1+z)^{t-s}
=\sum_{k\ge0}M_{i,k}(t)z^k,
\]

\[
M_{i,k}(t)=\sum_{\substack{s<t\\a_s=i}}\binom{t-s}{k}.
\]

Die Greedy-Regel vergleicht somit die ganzzahligen Vektoren
(M_i,0, M_i,1, M_i,2, ...) lexikografisch: Der erste unterschiedliche
Koeffizient entscheidet; kleiner bedeutet früher am Zug.

Für die Aktualisierung gilt exakt

\[
M_{i,k}(t+1)=M_{i,k}(t)+M_{i,k-1}(t)
+\mathbf1_{a_t=i}\binom1k,
\]

wobei M_i,−1 = 0. Das folgt unmittelbar aus der Pascalschen Identität.
Koeffizienten bis zum Grad d entwickeln sich unabhängig von den höheren
Koeffizienten. Ein abgeschnittener Vektor bestimmt die echte Entscheidung,
sofern sein lexikografisches Minimum bereits eindeutig ist.

## 2. Allgemeines Lemma: Permutation und Umkehrung

**Lemma.** Für jedes N besteht jeder an Index 2Nm beginnende Block aus
einer Permutation π der Spieler und anschließend ihrer Umkehrung:

\[
\pi\,\operatorname{rev}(\pi).
\]

An jeder solchen Blockgrenze sind die Momente M_i,0 und M_i,1 für alle
Spieler gleich.

**Beweis.** Am Anfang sind alle diese Werte null. Angenommen, sie sind an
einer Blockgrenze gleich. Weil der Grad-0-Koeffizient die bisherige Zugzahl
zählt, erhält in den nächsten N Zügen jeder Spieler genau einen Zug.
Unter den noch nicht ausgewählten Spielern ändert das bloße Altern die
Ordnung ihrer G_i nicht: Es multipliziert alle mit demselben positiven
Faktor. Daher ist die erste Runde eine feste Permutation π.

Sei r_i die Position von Spieler i in dieser Permutation, mit 0 ≤ r_i < N.
Nach der ersten Runde sind die Zugzahlen wieder gleich. Die zuvor
gleichen ersten Momente unterscheiden sich jetzt allein durch die Alter
N−r_i der gerade vergebenen Züge. Das kleinste erste Moment hat der
zuletzt berücksichtigte Spieler. Folglich erzwingt der Grad-1-Vergleich
die umgekehrte Reihenfolge in der nächsten Runde. Bereits berücksichtigte
Spieler scheiden durch ihre größere Zugzahl aus.

Am Ende des Doppelblocks besitzt jeder Spieler zwei neue Züge mit den
Altern

\[
2N-r_i\quad\text{und}\quad r_i+1.
\]

Ihre Summe ist immer 2N+1. Zugzahl und erstes Moment sind wieder bei allen
Spielern gleich. Induktion beweist das Lemma. ∎

### Aktualisierung an Blockgrenzen

Subtrahiere Spieler 0 als gemeinsame Referenz:

\[
D_{i,k}=M_{i,k}-M_{0,k}.
\]

An Blockgrenzen gilt D_i,0 = D_i,1 = 0. Mit B = 2N und

\[
w_k(r)=\binom{B-r}{k}+\binom{r+1}{k}
\]

lautet die exakte Aktualisierung

\[
D'_{i,k}=\sum_{j=2}^{k}\binom{B}{k-j}D_{i,j}
+w_k(r_i)-w_k(r_0).
\]

Für die Grade 2, 3 und 4 bedeutet dies

\[
\begin{aligned}
D'_{i,2}&=D_{i,2}+w_2(r_i)-w_2(r_0),\\
D'_{i,3}&=D_{i,3}+B D_{i,2}+w_3(r_i)-w_3(r_0),\\
D'_{i,4}&=D_{i,4}+B D_{i,3}+\binom B2D_{i,2}
+w_4(r_i)-w_4(r_0).
\end{aligned}
\]

Diese drei Formeln sind die gesamte Dynamik des beigefügten Prüfers.
Wenn sie eine Ordnung nicht entscheiden, bricht er ab; er ersetzt einen
unbekannten höheren Koeffizienten niemals durch eine willkürliche Wahl.

## 3. Vollständiger Beweis für N = 3

Schreibe A, B, C für die Spieler 0, 1, 2. Setze

\[
x_i=D_{i,2},\qquad y_i=D_{i,3},\qquad z_i=D_{i,4}.
\]

Der Referenzspieler A hat immer (x_A,y_A,z_A) = (0,0,0).
Die Ranggewichte sind

\[
w_2=(15,11,9),\qquad w_3=(20,10,5),\qquad w_4=(15,5,1).
\]

Damit gilt

\[
\begin{aligned}
x'_i&=x_i+w_2(r_i)-w_2(r_A),\\
y'_i&=y_i+6x_i+w_3(r_i)-w_3(r_A),\\
z'_i&=z_i+6y_i+15x_i+w_4(r_i)-w_4(r_A).
\end{aligned}
\]

### 3.1 Der endliche Anfang

Die folgende Tabelle ist aus diesen drei ganzzahligen Formeln direkt
nachrechenbar. π bezeichnet die erste Hälfte des jeweils folgenden
Sechserblocks.

| Index t | x_B | x_C | y_B | y_C | z_B | z_C | π |
|---:|---:|---:|---:|---:|---:|---:|:---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | ABC |
| 6 | −4 | −6 | −10 | −15 | −10 | −14 | CBA |
| 12 | −2 | 0 | −29 | −36 | −126 | −180 | BCA |
| 18 | 4 | 2 | −26 | −31 | −316 | −392 | ACB |
| 24 | −2 | −2 | −17 | −29 | −426 | −558 | CBA |
| 30 | 0 | 4 | −24 | −26 | −554 | −748 | BAC |
| 36 | 4 | 2 | −14 | −7 | −688 | −848 | ACB |
| 42 | −2 | −2 | −5 | −5 | −726 | −870 | CBA |
| 48 | 0 | 4 | −12 | −2 | −782 | −916 | BAC |

Nur der Start ist ein vollständiger Gleichstand. Bei t = 42 sind B und C
bis Grad 3 gleich, aber der vierte Koeffizient −870 < −726 entscheidet
für C vor B. Das ist der Grund, warum man nicht von Anfang an einfach alle
Koeffizienten oberhalb von Grad 3 verwerfen darf.

Die ersten 48 Zeichen lauten daher

```text
ABCCBA CBAABC BCAACB ACBBCA CBAABC BACCAB ACBBCA CBAABC
```

### 3.2 Der unendliche Rest

Ab t = 48 genügen dagegen die beiden Koordinaten x und y für sämtliche
Ordnungsvergleiche in der folgenden Tabelle:

| Index t | (x_B, y_B) | (x_C, y_C) | Nächste sechs Züge |
|---:|:---|:---|:---|
| 48 | (0, −12) | (4, −2) | BACCAB |
| 54 | (4, −2) | (2, 17) | ACBBCA |
| 60 | (−2, 7) | (−2, 19) | BCAACB |
| 66 | (4, 10) | (0, 12) | ACBBCA |
| 72 | (−2, 19) | (−4, 2) | CBAABC |
| 78 | (0, 12) | (2, −7) | ABCCBA |
| 84 | (−4, 2) | (−4, −10) | CBAABC |
| 90 | (−2, −17) | (2, −19) | BACCAB |
| 96 | (2, −19) | (0, −12) | CABBAC |
| 102 | (0, −12) | (4, −2) | Zustand von t = 48 |

In jeder Zeile sind die drei Paare (0,0), (x_B,y_B), (x_C,y_C)
verschieden. Deshalb steht die Reihenfolge eindeutig fest, unabhängig
von allen höheren Momenten. Zum Beispiel ist bei t = 48

\[
(0,-12)<_{\mathrm{lex}}(0,0)<_{\mathrm{lex}}(4,-2),
\]

also lautet π = BAC und der Doppelblock BACCAB.

Nach neun Doppelblöcken, also 54 Zügen, sind die entscheidenden vier
Koordinaten wieder genau dieselben. Ihre Aktualisierung benötigt weder
die absolute Zeit noch höhere Koeffizienten. Induktion beweist deshalb

\[
a_{t+54}=a_t\qquad\text{für alle }t\ge48.
\]

Der dauerhaft wiederholte Block ab diesem Index ist

```text
BACCAB ACBBCA BCAACB ACBBCA CBAABC ABCCBA CBAABC BACCAB CABBAC
```

Damit ist die unendliche Periodizität bewiesen, nicht nur ein weiteres
endliches Stück berechnet.

### 3.3 Kleinste Periode und Anfangsindex

Die vorangehenden Zeichen stimmen ebenfalls überein: a_47 = a_101 = C.
Also beginnt die Periodizität bereits bei Index 47, dem 48. Glied.
Noch einen Schritt früher gilt aber a_46 = B und a_100 = A.

Der angegebene 54erblock ist primitiv. Jeder echte Teiler von 54 teilt
entweder 18 oder 27; beide möglichen übergeordneten Teilperioden scheitern
bereits am ersten Zeichen, denn der Block beginnt mit B, während seine
Zeichen an den nullbasierten Positionen 18 und 27 jeweils A sind.
Jede kleinste Periode eines 54-periodischen unendlichen Wortes teilt 54.
Folglich ist die kleinste Periode genau 54.

Auch ein größerer Periodenwert könnte den Beginn nicht vor Index 47
verschieben: Jede Periode dieses schließlich primitiven 54-periodischen
Restes ist ein Vielfaches von 54, und die entsprechende Restposition
nach Index 46 enthält stets A statt B. Die minimale Vorlauflänge ist
damit 47.

## 4. Allgemeines Zwei-Zyklen-Kriterium

Für größere N müssen selbst die ersten vier Momentdifferenzen nicht
als vollständiger Zustand wiederkehren. Einzelne Koordinaten dürfen
driften, ohne dass sich die Entscheidungen ändern. Dafür genügt das
folgende stärkere Kriterium.

**Satz.** Gegeben seien ein verifiziertes Greedy-Präfix und ein
vorgeschlagener wiederholter Block der Länge L. Fixiere eine Phase dieses
Blocks und einen dort erforderlichen Vergleich zweier Spieler i, j.
Sei F_k(z) die Differenz G_j−G_i an dieser Phase nach k Wiederholungen
des vorgeschlagenen Blocks, zunächst als formal vorgeschriebene Folge
berechnet. Dann gilt

\[
F_{k+1}(z)=(1+z)^L F_k(z)+C(z),
\]

wobei C(z) nicht von k abhängt.

Sei d der kleinste Grad, in dem F_0 oder F_1 einen von null
verschiedenen Koeffizienten besitzt. Setze

\[
a=[z^d]F_0(z),\qquad b=[z^d]\bigl(F_1(z)-F_0(z)\bigr).
\]

Dann sind alle niedrigeren Koeffizienten für jedes k null, und

\[
[z^d]F_k(z)=a+kb.
\]

Insbesondere bleibt der Vergleich für alle k ≥ 0 strikt richtig,
wenn a ≥ 0, b ≥ 0 und F_0 bereits strikt positiv im lexikografischen
Sinn ist. Hierbei können a und b nicht beide null sein, weil d
gerade als erster auftretender Grad definiert wurde.

**Beweis.** Während der nächsten L Züge altern alle alten Beiträge um L;
das multipliziert sie mit (1+z)^L. Die während dieser L Züge neu
hinzukommenden Beiträge besitzen an der betrachteten Phase immer
dieselben Alter und Spielerzuordnungen. Ihre Differenz ist daher ein
festes C(z). Das beweist die Rekursion.

Da der konstante Koeffizient von (1+z)^L gleich 1 ist, ist diese
Rekursion bezüglich der Koeffizienten dreieckig. Für jeden Grad j < d
sind die Koeffizienten in F_0 und F_1 null. Induktiv über j folgt
C_j = 0 und anschließend F_k,j = 0 für alle k. Auf Grad d bleibt daher
nur die additive Rekursion

\[
F_{k+1,d}=F_{k,d}+C_d,
\qquad C_d=F_{1,d}-F_{0,d}=b.
\]

Sie ergibt a+kb. Ist a > 0, ist dieser Ausdruck unter b ≥ 0 immer
positiv. Ist a = 0, muss b > 0 sein; dann entscheidet dieser Grad für
jedes k ≥ 1, und für k = 0 gilt die separat überprüfte Positivität von
F_0. Höhere Koeffizienten können einen bereits strikt positiven ersten
Koeffizienten nicht umkehren. ∎

### Anwendung auf die tatsächliche Greedy-Folge

Der vorgeschlagene periodische Rest ist zunächst nur ein Kandidat.
Überprüft man das Kriterium für alle erforderlichen Vergleiche an jeder
Phase, folgt durch Induktion über die Züge, dass die echte Greedy-Regel
immer genau diesen Kandidaten erzeugt. Es liegt daher kein Zirkelschluss
durch die angenommene Wiederholung vor.

Wegen des Doppelblock-Lemmas reicht es, an jeder Blockgrenze die
N−1 benachbarten Spieler der vorgeschlagenen Permutation zu vergleichen.
Diese Vergleiche bestimmen die vollständige strikte Ordnung. Die
Umkehrung in der zweiten Hälfte folgt bereits aus dem Lemma.

**Zwei simulierte Wiederholungen allein reichen nicht.** Entscheidend
ist die bewiesene Formel a+kb und insbesondere das Vorzeichen b ≥ 0.
Beispielsweise sehen die Werte 2 und 1 für die ersten zwei Wiederholungen
noch richtig aus; die zugehörige Formel 2−k scheitert später.

## 5. Exakte Zertifikate für 3 ≤ N ≤ 24

Der Prüfer `fair_share_verify.py` und die Daten
`fair_share_certificates.json` gehören zu dieser Ausarbeitung.

Er rekonstruiert für jede Spielerzahl den Anfang aus dem Nullzustand,
überprüft dabei jeden benötigten Vergleich bis Grad 4, berechnet den
vorgeschlagenen Rest zweimal und prüft danach die Ungleichungen des
Zwei-Zyklen-Satzes. Alle Zahlen sind Python-Ganzzahlen beliebiger Größe.
Es gibt weder Gleitkommazahlen noch eine numerische Wahl eines kleinen p.

Die Blockzertifikate beweisen zunächst einen ausreichenden Startindex und
eine gültige Periode. Zusätzlich bestimmt der Prüfer die kleinste Periode
des zyklischen Wortes mit der exakten Präfixfunktion. Beim Rekonstruieren
des Anfangs vergleicht er jeden Zug mit der rückwärts fortgesetzten
periodischen Endfolge. Eins plus der letzte abweichende Index ist die
minimale Vorlauflänge. Denn jede andere spätere Periode muss ein
Vielfaches der kleinsten Endperiode sein und würde an diesem letzten
abweichenden Index denselben falschen Buchstaben verlangen.

Alle Längen in der Tabelle zählen einzelne Züge. Die Vorlauflänge ist
zugleich der nullbasierte Index, an dem die permanente Periode beginnt.

| N | Minimale Vorlauflänge | Kleinste Periode | Start des Blockzertifikats |
|---:|---:|---:|---:|
| 3 | 47 | 54 | 48 |
| 4 | 46 | 192 | 48 |
| 5 | 588 | 500 | 590 |
| 6 | 1197 | 864 | 1200 |
| 7 | 207 | 168 | 210 |
| 8 | 2429 | 512 | 2432 |
| 9 | 14468 | 4860 | 14472 |
| 10 | 5374 | 1600 | 5380 |
| 11 | 764 | 1056 | 770 |
| 12 | 66258 | 5184 | 66264 |
| 13 | 1007 | 936 | 1014 |
| 14 | 4380121 | 32928 | 4380124 |
| 15 | 330741 | 48600 | 330750 |
| 16 | 2822039 | 67584 | 2822048 |
| 17 | 1219 | 15708 | 1224 |
| 18 | 2781674 | 54432 | 2781684 |
| 19 | 432243 | 118560 | 432250 |
| 20 | 3752 | 28800 | 3760 |
| 21 | 19032663 | 26460 | 19032678 |
| 22 | 3156 | 34848 | 3168 |
| 23 | 309612 | 63480 | 309626 |
| 24 | 50652467 | 532224 | 50652480 |

Ausführung mit Python 3, ohne Zusatzpakete:

```sh
python3 fair_share_verify.py fair_share_certificates.json
```

Nur ausgewählte Fälle:

```sh
python3 fair_share_verify.py fair_share_certificates.json 3 4 15
```

Der aufwendige Teil ist die Rekonstruktion langer Vorläufe. Die Prüfung
des unendlichen Restes selbst benötigt für jeden Fall lediglich zwei
vorgeschriebene Wiederholungen und die bewiesene Koeffizientenformel.

Der beigefügte Prüfbericht `fair_share_verification.json` enthält die
Ergebnisse des separat geschriebenen Zwei-Zyklen-Prüfers. Die
Zertifikatsuche benutzte eine andere Implementierung mit exakten
Polynomen in der Wiederholungszahl. Zusätzlich wurden N = 3 und N = 4
unabhängig über volle Polynome beziehungsweise symbolische Summen
gegengeprüft.

Für N = 24 ergibt die unabhängige Prüfung insbesondere eine minimale
Vorlauflänge von **50652467 Zügen** und eine kleinste Periode von
**532224 Zügen**. Die permanente Periode beginnt also mit dem
50652468. Zug bei Zählung ab eins. Bei dieser Greedy-Regel ist der
Vorlauf für 24 Spieler damit keineswegs kurz.

## 6. Eine scheinbare Schleife, die später bricht

Bei N = 15 findet man ab Index 30600 einen Kandidaten mit Länge 8100.
Er wird 25-mal vollständig wiederholt und sieht deshalb sehr stabil
aus. Trotzdem endet diese Wiederholung später.

An Phase 219 der 270 Doppelblöcke des Kandidaten entscheidet der
vierte Alterskoeffizient über die Reihenfolge der nullbasierten Spieler
8 und 5. Unter der hypothetischen ewigen Wiederholung ist die
entscheidende Differenz

\[
30317118-1215000k.
\]

Für k = 0, ..., 24 ist sie positiv, für k = 25 negativ. Höhere
Koeffizienten können dieses Vorzeichen nicht ändern, da alle
niedrigeren Differenzen null sind. Tatsächlich liegt die erste
Abweichung vom vorgeschlagenen Wort an Index

\[
30\bigl(1020+25\cdot270+219\bigr)=239670.
\]

Der Kandidat verlangt dort Spieler 8, die echte Greedy-Regel wählt
Spieler 5. Die später zertifizierte Periode beträgt 48600, mit einem
ausreichenden Startindex 330750.

Das widerlegt **diesen vorgeschlagenen 8100erblock**, nicht die
schließliche Periodizität für N = 15. Es zeigt konkret, warum auch
zahlreiche beobachtete Wiederholungen keinen Unendlichkeitsbeweis
ersetzen. Die Angaben beziehen sich auf die hier exakt berechnete
Folge; es wird nicht unterstellt, dass das Video genau diesen Block
als endgültige Periode ausweist.

## 7. Was für beliebiges N bereits gilt und was noch fehlt

Für jede Spielerzahl gibt es einen allgemeinen endlichen Anteil der
Dynamik. Betrachte an Doppelblockgrenzen die sortierten zweiten
Momente. Ziehe ihr Minimum ab und teile durch 2. Diese Unterschiede
sind ganzzahlig. Die Ranggewichte, nach Abzug eines gemeinsamen Terms
und Division durch 2, sind

\[
w_r=\frac{(N-1-r)(N-r)}2,
\qquad 0\le r<N.
\]

Die kleinste aktuelle Last bekommt das größte Gewicht usw.
Bei gleichen Lasten beeinflusst die Entscheidung höherer Momente zwar
die Spielernamen, aber nicht das entstehende unbeschriftete Multiset.
Die sortierte, normalisierte Folgelast ist daher eine deterministische
Funktion der aktuellen sortierten, normalisierten Last.

Setze M = N(N−1)/2. Die Spannweite der Lasten bleibt höchstens M.
Denn für zwei geordnete Lasten ℓ_i ≤ ℓ_j sind die Gewichte umgekehrt
geordnet, w_i ≥ w_j; die neue Differenz ist

\[
(\ell_i+w_i)-(\ell_j+w_j)
=-(\ell_j-\ell_i)+(w_i-w_j),
\]

und liegt zwischen der negativen alten Spannweite und M. Die neue
Spannweite überschreitet somit das Maximum aus alter Spannweite und M
nicht. Zu Beginn ist sie null.

Es gibt folglich höchstens

\[
\binom{M+N-1}{N-1}
\]

sortierte, normalisierte Zustände: Der erste Eintrag ist null, die
übrigen N−1 Einträge stammen nicht absteigend aus {0,...,M}.
Diese **unbeschriftete Konfiguration der zweiten Momente** wird daher
für jedes N schließlich periodisch.

Der fehlende Schritt betrifft die Namen der Spieler bei Gleichständen.
Diese Entscheidungen hängen von höheren Momenten ab. Aus einem
periodischen Multiset zweiter Momente folgt keine periodische Folge
von Spielernamen. Schon N = 2 zeigt, dass das Übergehen dieser
Unterscheidung einen falschen Beweis erzeugen würde.

Um die allgemeine Vermutung zu beweisen, benötigt man beispielsweise
einen Satz, der für jedes N ≥ 3 das Erreichen eines gültigen
Periodizitätszertifikats garantiert. Ein solcher Satz wird hier nicht
hergeleitet. Die exakten Einzelfallbeweise und das Zertifizierungskriterium
sind vollständig; der universelle Existenzschritt bleibt offen.

## 8. Literatur und historische Einordnung

Eine Suche bis 2026-11-26 lieferte keinen veröffentlichten Beweis für
alle N ≥ 3. Das ist eine Aussage über das Rechercheergebnis, kein
Beweis dafür, dass kein solcher Text existiert.

- Joshua N. Cooper und Aaron M. Dutle, *Greedy Galois Games*,
  American Mathematical Monthly 120 (2013), 441–451.
  [arXiv:1110.1137](https://arxiv.org/abs/1110.1137),
  [Autorenfassung](https://people.math.sc.edu/cooper/ThueMorseDueling.pdf).
  Der einschlägige bewiesene Grenzwertsatz behandelt zwei Spieler.
- [OEIS A287150](https://oeis.org/A287150): die Dreispielerfolge.
  Der gelesene Eintrag beschreibt die Periodizität als Beobachtung der
  ersten 5000 Glieder und nennt den 54erblock ab dem 48. Glied.
- kram1032, [*What's the fairest turn sequence for n players?*](https://math.stackexchange.com/questions/2078609/whats-the-fairest-turn-sequence-for-n-players),
  Mathematics Stack Exchange: die konkrete Koeffizientenregel und
  ihre programmatische Umsetzung.
- Anders Kaseorg, Kommentar von 2012-11-01 unter Zachary Abels
  [*Dueling Dilettantes*](https://blog.zacharyabel.com/2012/02/dueling-dilettantes/):
  meldet bereits die beobachteten Perioden 54, 192, 500 und 864 für
  drei bis sechs Spieler. Die Dokumentation reicht somit weiter
  zurück als der OEIS-Eintrag von 2017.
- A. Zabolotskii, *Плохие стрелки* (»Schlechte Schützen«), Kvant 2022,
  Nr. 7, S. 22–24,
  [offizielle Artikelseite](https://www.kvant.digital/issues/2022/7/zabolotskiy-plohie_strelki-99fb3197/),
  [DOI:10.4213/kvant20220702](https://doi.org/10.4213/kvant20220702).
  Der Beitrag stellt die Periodizität für drei und mehr Spieler
  ausdrücklich als offene Aufgabe dar. Dies beschreibt den Stand
  des Artikels von 2022.
- Tanya Khovanova und Tejo Madhavarapu, *Fair Duels after a False Start*,
  [arXiv:2610.00880v1](https://arxiv.org/html/2610.00880v1), 2026-10-01.
  Satz 1.1 behandelt zwei Spieler mit vorgegebenem endlichem Anfang,
  der weder ein Thue–Morse-Präfix noch dessen Komplement ist.
  Er ist kein Satz für beliebig viele Spieler.

Die vorliegenden Einzelfallbeweise sind mit dieser historischen
Einordnung vereinbar: Ein endliches exaktes Zertifikat kann einen
bestimmten Fall lösen, ohne die allgemeine Existenzbehauptung zu lösen.
