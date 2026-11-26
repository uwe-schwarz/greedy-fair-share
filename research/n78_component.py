"""Exact isolated-component analysis for N=78; not a full N=78 certificate."""

from fractions import Fraction
import json

from transport_components import transport, prefix_rows, binary_return, shifted_sum


def main():
    n = 78
    degree = 8
    mu, cycle, weights, components = transport(n)
    component = next(c for c in components
                     if c["size"] == 2 and c["ranks_at_phase_0"] == [6, 7])
    phase = component["tie_phases"][0]
    returns = [binary_return(n, cycle, weights, component["rank_paths"], p, degree)
               for p in component["tie_phases"]]
    assert all(r["rank_path_A_B"] == returns[0]["rank_path_A_B"] for r in returns)
    ret = returns[0]
    rows = prefix_rows(n, mu + phase, degree)
    order = sorted(range(n), key=lambda i: (rows[i], i))
    a, b = [order[r] for r in component["rank_paths"][phase]]
    d = [y - x for x, y in zip(rows[a], rows[b])]
    initial = d[:]
    h = ret["H_coefficients_z_0_to_8"]
    length = ret["blocks"] * 2 * n
    assert d[:3] == h[:3] == [0, 0, 0]
    assert d[3] > 0 > h[3]
    count, remainder = divmod(d[3], -h[3])
    assert remainder == 0
    for _ in range(count):
        assert d[3] > 0
        d = [v + delta for v, delta in zip(shifted_sum(d, length, degree), h)]
    assert d[3] == 0 and d[4] > 0
    zero_block = mu + phase + count * ret["blocks"]
    effective_k4 = -length * h[3]
    quotient, remainder4 = divmod(d[4], effective_k4)
    assert 0 < remainder4 < effective_k4
    stable_block = zero_block + 2 * ret["blocks"] * quotient
    result = {
        "scope": "One closed binary comparison component; not the full N=78 sequence",
        "n": n,
        "base_preperiod_blocks": mu,
        "base_period_blocks": len(cycle),
        "component_phase_0_ranks": [6, 7],
        "fixed_player_labels_A_B": [a, b],
        "first_comparison_block": mu + phase,
        "return_blocks": ret["blocks"],
        "return_turns": length,
        "same_rank_paths_at_every_comparison": True,
        "rank_path_A_B": ret["rank_path_A_B"],
        "initial_D_coefficients_z_0_to_8": initial,
        "H_coefficients_z_0_to_8": h,
        "returns_to_first_third_moment_zero": count,
        "first_third_moment_zero_block": zero_block,
        "first_third_moment_zero_turn": zero_block * 2 * n,
        "D_at_zero_coefficients_z_0_to_8": d,
        "fourth_moment_decides": True,
        "two_return_fourth_coefficient_step": effective_k4,
        "ratio_at_zero": str(Fraction(d[4], effective_k4)),
        "further_two_return_steps_to_strict_cycle": quotient,
        "nonzero_fourth_residue": remainder4,
        "sufficient_component_stabilization_block": stable_block,
        "sufficient_component_stabilization_turn": stable_block * 2 * n,
        "valid_component_period_blocks": 4 * ret["blocks"],
        "valid_component_period_turns": 4 * ret["blocks"] * 2 * n,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
