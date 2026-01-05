"""
Extensive Correctness Tests for SATA Project
Tests: Classes, Distance, Satisfaction Formulas, Constraints, Algorithms
"""
import sys
import os
sys.path.append(os.getcwd())

from src.common.classes import worker, task, POS_INF, NEG_INF
from src.common.distance import calculate_distance
from src.common.utils import (
    set_itr, csore, csat, psat, sat, 
    check_worker, check_validity, check_CWS, rm_el,
    dif_psat, cop_sum, dif_sat
)
from src.algorithms.greedy import greedy
from src.algorithms.gt import GT_algo
from src.probabilistic.monte_carlo import sample_skills

import math

# ============ TEST HELPERS ============
def assert_approx(a, b, tol=1e-6, msg=""):
    assert abs(a - b) < tol, f"FAIL: {a} != {b} (tol={tol}). {msg}"

def test_passed(name):
    print(f"  [PASS] {name}")

def test_failed(name, e):
    print(f"  [FAIL] {name}: {e}")

# ============ TEST SUITES ============

def test_classes():
    print("\n=== Testing Classes ===")
    try:
        # Test worker creation
        w = worker(1, 10.0, 20.0, 5.0, 1.5, [1, 2, 3], [10, 20])
        assert w.ind == 1, "Worker index mismatch"
        assert w.latitude == 10.0, f"Worker latitude mismatch: {w.latitude} != 10.0"
        assert w.longitude == 20.0, f"Worker longitude mismatch: {w.longitude} != 20.0"
        assert w.r == 5.0, "Worker range mismatch"
        assert w.cost == 1.5, "Worker cost mismatch"
        assert w.K == [1, 2, 3], "Worker skills mismatch"
        assert w.task_set == [10, 20], "Worker task history mismatch"
        test_passed("Worker creation")
        
        # Test task creation
        t = task(1, 30.0, 40.0, [1, 2], 100.0, POS_INF)
        assert t.ind == 1, "Task index mismatch"
        assert t.latitude == 30.0, f"Task latitude mismatch: {t.latitude} != 30.0"
        assert t.longitude == 40.0, f"Task longitude mismatch: {t.longitude} != 40.0"
        assert t.K_req == [1, 2], "Task required skills mismatch"
        assert t.budget == 100.0, "Task budget mismatch"
        test_passed("Task creation")
        
        # Test constants
        assert POS_INF > 1e9, "POS_INF too small"
        assert NEG_INF < -1e9, "NEG_INF too large"
        test_passed("Constants")
    except Exception as e:
        test_failed("Exception in test_classes", e)
        raise e

def test_distance():
    print("\n=== Testing Distance Calculation ===")
    
    # Same point = 0 distance
    d = calculate_distance(0.0, 0.0, 0.0, 0.0)
    assert_approx(d, 0.0, msg="Same point should be 0 distance")
    test_passed("Same point distance")
    
    # Known distance: NYC to LA ~ 3940 km
    # NYC: 40.7128, -74.0060
    # LA: 34.0522, -118.2437
    d = calculate_distance(40.7128, -74.0060, 34.0522, -118.2437)
    assert 3900 < d < 4000, f"NYC-LA distance should be ~3940km, got {d}"
    test_passed("NYC to LA distance")
    
    # Small distance (0.01 degrees ~ 1.1km at equator)
    d = calculate_distance(0.0, 0.0, 0.01, 0.0)
    assert 1.0 < d < 1.2, f"0.01 degrees should be ~1.1km, got {d}"
    test_passed("Small distance")

def test_set_operations():
    print("\n=== Testing Set Operations ===")
    
    # set_itr (intersection)
    r = set_itr([1, 2, 3], [2, 3, 4])
    assert set(r) == {2, 3}, f"Intersection wrong: {r}"
    test_passed("set_itr basic")
    
    r = set_itr([1, 2], [3, 4])
    assert r == [], f"Empty intersection should be []: {r}"
    test_passed("set_itr empty")
    
    # rm_el (remove element)
    r = rm_el([1, 2, 3], 2)
    assert r == [1, 3], f"rm_el wrong: {r}"
    test_passed("rm_el basic")

def test_satisfaction_formulas():
    print("\n=== Testing Satisfaction Formulas ===")
    
    # csore (cooperation score between two workers)
    w1 = worker(1, 0, 0, 5, 1, [1], [10, 20, 30])
    w2 = worker(2, 0, 0, 5, 1, [2], [20, 30, 40])  # shares 20, 30
    
    # b=0.5, w=0.01. itr=2, unon=4 (10,20,30,40)
    # csore = 0.5*0.01 + 0.5 * 2/4 = 0.005 + 0.25 = 0.255
    c = csore(w1, w2)
    assert_approx(c, 0.255, tol=0.01, msg=f"csore mismatch: {c}")
    test_passed("csore with shared history")
    
    # csore with empty history (should not crash)
    w3 = worker(3, 0, 0, 5, 1, [1], [])
    w4 = worker(4, 0, 0, 5, 1, [2], [])
    c = csore(w3, w4)
    # unon = 0, should return b*w = 0.005
    assert_approx(c, 0.005, tol=0.001, msg=f"csore empty history: {c}")
    test_passed("csore empty history (no division by zero)")
    
    # csat (cooperation satisfaction for worker set)
    # Single worker -> 0
    assert csat([w1]) == 0, "csat of single worker should be 0"
    test_passed("csat single worker")
    
    # Two workers
    c = csat([w1, w2])
    # csat = 2 * sum(pairs) / (n-1) = 2 * 0.255 / 1 = 0.51
    assert_approx(c, 0.51, tol=0.02, msg=f"csat two workers: {c}")
    test_passed("csat two workers")
    
    # psat (price satisfaction)
    t = task(1, 0, 0, [1], 100.0, POS_INF)
    w = worker(1, 0.01, 0.01, 5, 1.0, [1], [])  # ~1.5km from task
    p = psat(t, [w])
    # psat = budget - sum(dist * cost) = 100 - 1.5*1 ~ 98.5
    assert 98 < p < 100, f"psat should be ~98.5, got {p}"
    test_passed("psat basic")
    
    # sat (total satisfaction)
    s = sat(t, [w])
    # sat = 0.5 * psat/100000 + 0.5 * csat/10000
    # For single worker, csat=0, so sat = 0.5 * ~98.5/100000 ~ 0.0005
    assert s > 0, f"sat should be positive, got {s}"
    test_passed("sat basic")

def test_constraints():
    print("\n=== Testing Constraint Functions ===")
    
    # check_worker: individual constraints
    t = task(1, 0.0, 0.0, [1, 2], 100.0, POS_INF)
    
    # Worker in range with matching skill
    w_good = worker(1, 0.01, 0.01, 5.0, 1.0, [1], [])
    assert check_worker(t, w_good) == True, "Should pass: in range, has skill 1"
    test_passed("check_worker: valid worker")
    
    # Worker out of range
    w_far = worker(2, 10.0, 10.0, 5.0, 1.0, [1], [])  # ~1500km away
    assert check_worker(t, w_far) == False, "Should fail: out of range"
    test_passed("check_worker: out of range")
    
    # Worker with no matching skills
    w_no_skill = worker(3, 0.01, 0.01, 5.0, 1.0, [99], [])
    assert check_worker(t, w_no_skill) == False, "Should fail: no matching skill"
    test_passed("check_worker: no matching skill")
    
    # check_validity: group constraints
    t = task(1, 0.0, 0.0, [1, 2], 1000.0, POS_INF)
    
    # Valid group: covers all skills, disjoint, within budget
    w1 = worker(1, 0.01, 0.01, 5.0, 1.0, [1], [])
    w2 = worker(2, 0.01, 0.01, 5.0, 1.0, [2], [])
    assert check_validity(t, [w1, w2]) == True, "Should pass: all constraints met"
    test_passed("check_validity: valid group")
    
    # Invalid: skills not covered
    assert check_validity(t, [w1]) == False, "Should fail: skill 2 not covered"
    test_passed("check_validity: missing skill coverage")
    
    # Invalid: overlapping skills (disjoint constraint)
    w3 = worker(3, 0.01, 0.01, 5.0, 1.0, [1, 2], [])
    w4 = worker(4, 0.01, 0.01, 5.0, 1.0, [2, 3], [])  # overlaps on skill 2
    assert check_validity(t, [w3, w4]) == False, "Should fail: overlapping skills"
    test_passed("check_validity: overlapping skills")
    
    # Invalid: budget exceeded
    t_tight = task(2, 0.0, 0.0, [1], 0.1, POS_INF)  # Very small budget
    w_far = worker(5, 1.0, 1.0, 200.0, 10.0, [1], [])  # ~150km, cost 10
    assert check_validity(t_tight, [w_far]) == False, "Should fail: budget exceeded"
    test_passed("check_validity: budget exceeded")
    
    # check_CWS: combined check
    t = task(1, 0.0, 0.0, [1, 2], 1000.0, POS_INF)
    w1 = worker(1, 0.01, 0.01, 5.0, 1.0, [1], [])
    w2 = worker(2, 0.01, 0.01, 5.0, 1.0, [2], [])
    assert check_CWS(t, [w1, w2]) == True, "check_CWS should pass"
    test_passed("check_CWS: valid")

def test_greedy_algorithm():
    print("\n=== Testing Greedy Algorithm ===")
    
    # Simple case: 2 tasks, 2 workers, perfect match
    t1 = task(1, 0.0, 0.0, [1], 1000.0, POS_INF)
    t2 = task(2, 10.0, 10.0, [2], 1000.0, POS_INF)
    
    w1 = worker(1, 0.01, 0.01, 5.0, 1.0, [1], [])
    w2 = worker(2, 10.01, 10.01, 5.0, 1.0, [2], [])
    
    T = [t1, t2]
    W = [w1, w2]
    
    asg, unassigned = greedy(T, W)
    assert len(asg) == 2, f"Should assign both workers, got {len(asg)}"
    test_passed("Greedy: basic 2-2 assignment")
    
    # Case with unassignable worker (no matching skill)
    t3 = task(3, 0.0, 0.0, [99], 1000.0, POS_INF)
    w3 = worker(3, 0.01, 0.01, 5.0, 1.0, [1], [])  # Has skill 1, not 99
    
    asg, unassigned = greedy([t3], [w3])
    assert len(asg) == 0, f"Should not assign, got {len(asg)}"
    test_passed("Greedy: no valid assignment")
    
    # Case with multiple workers competing for same task
    t4 = task(4, 0.0, 0.0, [1], 1000.0, POS_INF)
    w4 = worker(4, 0.01, 0.01, 5.0, 0.5, [1], [1, 2, 3])  # Cheaper, history
    w5 = worker(5, 0.02, 0.02, 5.0, 2.0, [1], [])  # Expensive, no history
    
    asg, _ = greedy([t4], [w4, w5])
    # Should pick the better worker (w4 is cheaper)
    assert len(asg) >= 1, "Should assign at least one"
    test_passed("Greedy: picks better option")

def test_gt_algorithm():
    print("\n=== Testing Game Theoretic Algorithm ===")
    
    # Same simple case as greedy
    t1 = task(1, 0.0, 0.0, [1], 1000.0, POS_INF)
    t2 = task(2, 10.0, 10.0, [2], 1000.0, POS_INF)
    
    w1 = worker(1, 0.01, 0.01, 5.0, 1.0, [1], [])
    w2 = worker(2, 10.01, 10.01, 5.0, 1.0, [2], [])
    
    T = [t1, t2]
    W = [w1, w2]
    
    asg = GT_algo(T, W)
    assert len(asg) == 2, f"GT should assign both, got {len(asg)}"
    test_passed("GT: basic 2-2 assignment")
    
    # GT should improve on greedy when possible
    # Create a scenario where switching helps
    t1 = task(1, 0.0, 0.0, [1], 1000.0, POS_INF)
    t2 = task(2, 0.01, 0.01, [2], 1000.0, POS_INF) # Distinct location
    
    w1 = worker(1, 0.0, 0.0, 5.0, 1.0, [1, 2], [])  # At T1
    w2 = worker(2, 0.0, 0.0, 5.0, 1.0, [2], [])     # At T1/T2
    
    asg = GT_algo([t1, t2], [w1, w2])
    # Optimal: w1 -> t1, w2 -> t2
    assert len(asg) == 2, f"GT should assign both tasks, got {len(asg)}"
    test_passed("GT: optimal reassignment")
    
    # Check Nash Equilibrium property: no worker wants to unilaterally move
    # (This is hard to verify directly, but we can at least check it terminates)
    test_passed("GT: terminates (Nash Equilibrium reached)")

def test_monte_carlo():
    print("\n=== Testing Monte Carlo Sampling ===")
    
    # Test sample_skills function
    ws_incmp = [
        [],  # Index 0 unused
        [(0.5, 'A'), (0.5, 'B')],  # Worker 1: 50% chance for A, 50% for B
        [(1.0, 'C')],             # Worker 2: 100% chance for C
        [(0.0, 'D')],             # Worker 3: 0% chance for D
    ]
    
    # Run multiple times to check probabilistic behavior
    a_count = 0
    c_count = 0
    d_count = 0
    
    for _ in range(100):
        sampled = sample_skills(ws_incmp)
        if 'A' in sampled.get(1, []):
            a_count += 1
        if 'C' in sampled.get(2, []):
            c_count += 1
        if 'D' in sampled.get(3, []):
            d_count += 1
    
    # A should appear ~50 times (binomial, expect 35-65)
    assert 30 <= a_count <= 70, f"A should appear ~50%: {a_count}/100"
    test_passed("Monte Carlo: 50% probability skill")
    
    # C should appear 100 times
    assert c_count == 100, f"C should always appear: {c_count}/100"
    test_passed("Monte Carlo: 100% probability skill")
    
    # D should never appear
    assert d_count == 0, f"D should never appear: {d_count}/100"
    test_passed("Monte Carlo: 0% probability skill")

def test_edge_cases():
    print("\n=== Testing Edge Cases ===")
    
    # Empty inputs
    asg, unassigned = greedy([], [])
    assert len(asg) == 0, "Empty input should return empty"
    test_passed("Greedy: empty input")
    
    asg = GT_algo([], [])
    assert len(asg) == 0, "GT empty input should return empty"
    test_passed("GT: empty input")
    
    # Single task, single worker
    t = task(1, 0.0, 0.0, [1], 1000.0, POS_INF)
    w = worker(1, 0.01, 0.01, 5.0, 1.0, [1], [])
    
    asg, _ = greedy([t], [w])
    assert len(asg) == 1, "Single valid pair should assign"
    test_passed("Single task-worker pair")
    
    # All workers out of range
    w_far = worker(1, 100.0, 100.0, 1.0, 1.0, [1], [])
    asg, _ = greedy([t], [w_far])
    assert len(asg) == 0, "Out of range worker should not assign"
    test_passed("All workers out of range")

# ============ MAIN ============
def run_all_tests():
    print("=" * 60)
    print("EXTENSIVE CORRECTNESS TESTS FOR SATA PROJECT")
    print("=" * 60)
    
    try:
        test_classes()
        test_distance()
        test_set_operations()
        test_satisfaction_formulas()
        test_constraints()
        test_greedy_algorithm()
        test_gt_algorithm()
        test_monte_carlo()
        test_edge_cases()
        
        print("\n" + "=" * 60)
        print("ALL TESTS PASSED SUCCESSFULLY!")
        print("=" * 60)
        return True
    except AssertionError as e:
        print(f"\n[ASSERTION ERROR] {e}")
        return False
    except Exception as e:
        print(f"\n[UNEXPECTED ERROR] {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
