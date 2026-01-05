import sys
import os

# Add project root to sys.path explicitly to emulate running from root
sys.path.append(os.getcwd())

from src.common.classes import worker, task, POS_INF
from src.algorithms.greedy import greedy
from src.algorithms.gt import GT_algo
from src.common.utils import sat

def test_sanity():
    print("Setting up dummy data...")
    # Create 2 tasks
    # Task(ind, lon, lat, skills, budget, expiry)
    t1 = task(1, 0.0, 0.0, [1], 100.0, POS_INF)
    t2 = task(2, 10.0, 10.0, [2], 100.0, POS_INF)
    T = [t1, t2]

    # Create 3 workers
    # Worker(ind, lon, lat, range, cost, skills, history)
    # 0.01 deg approx 1.1 km. Range 5.0 covers it.
    w1 = worker(1, 0.01, 0.01, 5.0, 1.0, [1], [])
    w2 = worker(2, 10.01, 10.01, 5.0, 1.0, [2], [])
    w3 = worker(3, 5.0, 5.0, 1000.0, 0.5, [1, 2], []) # Can do both, huge range
    W = [w1, w2, w3]

    print("\n--- Testing Greedy Algorithm ---")
    asg_greedy, unassigned_greedy = greedy(T, W)
    print(f"Greedy Assignments: {len(asg_greedy)}")
    print(f"Greedy Unassigned: {len(unassigned_greedy)}")
    
    for w, t in asg_greedy:
        print(f"  Worker {w.ind} assigned to Task {t.ind}")

    assert len(asg_greedy) >= 2, "Greedy should assign both tasks"

    print("\n--- Testing Game Theoretic Algorithm ---")
    asg_gt = GT_algo(T, W)
    print(f"GT Assignments: {len(asg_gt)}")
    
    for w, t in asg_gt:
        print(f"  Worker {w.ind} assigned to Task {t.ind}")
        
    assert len(asg_gt) >= 2, "GT should assign both tasks"
    
    print("\nSanity Check Passed!")

if __name__ == "__main__":
    test_sanity()
