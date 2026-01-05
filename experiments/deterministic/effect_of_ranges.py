"""
Effect of Worker Range on Algorithm Performance
Analyzes how varying worker travel ranges affects assignments, satisfaction, and runtime.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import matplotlib.pyplot as plt
import time as tm
from src.common.classes import worker, task, POS_INF
from src.algorithms.greedy import greedy
from src.algorithms.gt import GT_algo
from src.common.utils import sat
from data.generators.gen_input import (
    n, m, budget, task_location, task_skills,
    worker_location, worker_cost, worker_skills, task_history
)
from data.generators.start import input_tasks, input_workers

def Cal_Sat(Asg):
    """Calculate total satisfaction score for all assignments."""
    return sum(sat(t, [w]) for w, t in Asg)

def run_experiment(range_multipliers):
    """Run experiments for different range multipliers."""
    base_range = 50.0  # Base range in km
    
    results = {
        'ranges': [base_range * mult for mult in range_multipliers],
        'greedy_assignments': [],
        'greedy_satisfaction': [],
        'greedy_time': [],
        'gt_assignments': [],
        'gt_satisfaction': [],
        'gt_time': []
    }
    
    for mult in range_multipliers:
        current_range = base_range * mult
        print(f"Running with range = {current_range} km...")
        
        # Create tasks (same for all experiments)
        T = []
        input_tasks(n, T, task_location, task_skills, budget)
        
        # Create workers with modified range
        modified_range = [current_range for _ in range(m+1)]
        W = []
        input_workers(m, W, worker_location, modified_range, worker_cost, worker_skills, task_history)
        
        # Run Greedy
        start = tm.time()
        Asg_greedy, _ = greedy(T, W)
        end = tm.time()
        results['greedy_assignments'].append(len(Asg_greedy))
        results['greedy_satisfaction'].append(Cal_Sat(Asg_greedy))
        results['greedy_time'].append(end - start)
        
        # Run GT
        start = tm.time()
        Asg_gt = GT_algo(T, W)
        end = tm.time()
        results['gt_assignments'].append(len(Asg_gt))
        results['gt_satisfaction'].append(Cal_Sat(Asg_gt))
        results['gt_time'].append(end - start)
    
    return results

def plot_results(results):
    """Generate visualization plots."""
    ranges = results['ranges']
    
    # Plot 1: Assignments vs Range
    plt.figure(figsize=(10, 6))
    plt.plot(ranges, results['greedy_assignments'], 'b-o', label='CAG (Greedy)', linewidth=2)
    plt.plot(ranges, results['gt_assignments'], 'r-s', label='GT', linewidth=2)
    plt.xlabel('Worker Range (km)', fontsize=12)
    plt.ylabel('Number of Assignments', fontsize=12)
    plt.title('Effect of Worker Range on Number of Assignments', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('experiments/deterministic/ranges_assignments.png', dpi=150)
    plt.show()
    
    # Plot 2: Satisfaction vs Range
    plt.figure(figsize=(10, 6))
    plt.plot(ranges, results['greedy_satisfaction'], 'b-o', label='CAG (Greedy)', linewidth=2)
    plt.plot(ranges, results['gt_satisfaction'], 'r-s', label='GT', linewidth=2)
    plt.xlabel('Worker Range (km)', fontsize=12)
    plt.ylabel('Total Satisfaction Score', fontsize=12)
    plt.title('Effect of Worker Range on Satisfaction Score', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('experiments/deterministic/ranges_satisfaction.png', dpi=150)
    plt.show()
    
    # Plot 3: Time vs Range
    plt.figure(figsize=(10, 6))
    plt.plot(ranges, results['greedy_time'], 'b-o', label='CAG (Greedy)', linewidth=2)
    plt.plot(ranges, results['gt_time'], 'r-s', label='GT', linewidth=2)
    plt.xlabel('Worker Range (km)', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.title('Effect of Worker Range on Running Time', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('experiments/deterministic/ranges_time.png', dpi=150)
    plt.show()

def print_results(results):
    """Print detailed results."""
    print("\n" + "="*70)
    print("RESULTS: Effect of Worker Range")
    print("="*70)
    
    for i, r in enumerate(results['ranges']):
        print(f"\n--- Range = {r} km ---")
        print(f"CAG: Assignments={results['greedy_assignments'][i]}, "
              f"Satisfaction={results['greedy_satisfaction'][i]:.4f}, "
              f"Time={results['greedy_time'][i]:.4f}s")
        print(f"GT:  Assignments={results['gt_assignments'][i]}, "
              f"Satisfaction={results['gt_satisfaction'][i]:.4f}, "
              f"Time={results['gt_time'][i]:.4f}s")

if __name__ == "__main__":
    range_multipliers = [0.5, 1.0, 1.5, 2.0]
    
    print("="*70)
    print("Effect of Worker Range on Algorithm Performance")
    print("="*70)
    
    results = run_experiment(range_multipliers)
    print_results(results)
    plot_results(results)
