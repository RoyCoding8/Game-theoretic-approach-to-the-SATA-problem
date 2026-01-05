import sys, os
sys.path.append(os.getcwd())

from src.common.classes import worker, task, POS_INF
from src.algorithms.greedy import greedy
from src.algorithms.gt import GT_algo

def test_sanity():
    print("Setting up dummy data...")
    
    t1 = task(1, 0.0, 0.0, [1], 100.0, POS_INF)
    t2 = task(2, 10.0, 10.0, [2], 100.0, POS_INF)
    T = [t1, t2]

    w1 = worker(1, 0.01, 0.01, 5.0, 1.0, [1], [])
    w2 = worker(2, 10.01, 10.01, 5.0, 1.0, [2], [])
    w3 = worker(3, 5.0, 5.0, 1000.0, 0.5, [1, 2], [])
    W = [w1, w2, w3]

    print("\n--- Greedy ---")
    asg_greedy, unassigned = greedy(T, W)
    print(f"Assignments: {len(asg_greedy)}, Unassigned: {len(unassigned)}")
    for w, t in asg_greedy:
        print(f"  W{w.ind} -> T{t.ind}")
    assert len(asg_greedy) >= 2

    print("\n--- GT ---")
    asg_gt = GT_algo(T, W)
    print(f"Assignments: {len(asg_gt)}")
    for w, t in asg_gt:
        print(f"  W{w.ind} -> T{t.ind}")
    assert len(asg_gt) >= 2
    
    print("\nPassed!")

if __name__ == "__main__":
    test_sanity()
