"""
Effect of Task Budget on Algorithm Performance
Analyzes how varying task budgets affects assignments, satisfaction, and runtime.
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
    worker_location, worker_range, worker_cost, worker_skills, task_history
)
from data.generators.start import input_tasks, input_workers

def Cal_Sat(Asg):
    """Calculate total satisfaction score for all assignments."""
    return sum(sat(t, [w]) for w, t in Asg)

def run_experiment(budget_values):
    """Run experiments for different budget values."""
    results = {
        'budgets': budget_values,
        'greedy_assignments': [],
        'greedy_satisfaction': [],
        'greedy_time': [],
        'gt_assignments': [],
        'gt_satisfaction': [],
        'gt_time': []
    }
    
    for b in budget_values:
        print(f"Running with budget = {b}...")
        
        # Create workers (same for all experiments)
        W = []
        input_workers(m, W, worker_location, worker_range, worker_cost, worker_skills, task_history)
        
        # Create tasks with modified budget
        T = []
        modified_budget = [b for _ in range(n+1)]
        input_tasks(n, T, task_location, task_skills, modified_budget)
        
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

def normalize_scores(scores):
    """Normalize satisfaction scores to 0-100 range."""
    mx = max(scores) if scores else 1
    mn = min(scores) if scores else 0
    if mx == mn:
        return [50] * len(scores)
    return [(s - mn) * 100 / (mx - mn) for s in scores]

def plot_results(results):
    """Generate visualization plots."""
    budgets = results['budgets']
    
    # Plot 1: Assignments vs Budget
    plt.figure(figsize=(10, 6))
    plt.plot(budgets, results['greedy_assignments'], 'b-o', label='CAG (Greedy)', linewidth=2)
    plt.plot(budgets, results['gt_assignments'], 'r-s', label='GT', linewidth=2)
    plt.xlabel('Task Budget', fontsize=12)
    plt.ylabel('Number of Assignments', fontsize=12)
    plt.title('Effect of Task Budget on Number of Assignments', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('experiments/deterministic/budget_assignments.png', dpi=150)
    plt.show()
    
    # Plot 2: Satisfaction vs Budget
    all_sat = results['greedy_satisfaction'] + results['gt_satisfaction']
    greedy_norm = normalize_scores(results['greedy_satisfaction'])
    gt_norm = normalize_scores(results['gt_satisfaction'])
    
    plt.figure(figsize=(10, 6))
    plt.plot(budgets, greedy_norm, 'b-o', label='CAG (Greedy)', linewidth=2)
    plt.plot(budgets, gt_norm, 'r-s', label='GT', linewidth=2)
    plt.xlabel('Task Budget', fontsize=12)
    plt.ylabel('Normalized Satisfaction Score (%)', fontsize=12)
    plt.title('Effect of Task Budget on Satisfaction Score', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('experiments/deterministic/budget_satisfaction.png', dpi=150)
    plt.show()
    
    # Plot 3: Time vs Budget
    plt.figure(figsize=(10, 6))
    plt.plot(budgets, results['greedy_time'], 'b-o', label='CAG (Greedy)', linewidth=2)
    plt.plot(budgets, results['gt_time'], 'r-s', label='GT', linewidth=2)
    plt.xlabel('Task Budget', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.title('Effect of Task Budget on Running Time', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('experiments/deterministic/budget_time.png', dpi=150)
    plt.show()

def print_results(results):
    """Print detailed results."""
    budgets = results['budgets']
    print("\n" + "="*70)
    print("RESULTS: Effect of Task Budget")
    print("="*70)
    
    for i, b in enumerate(budgets):
        print(f"\n--- Budget = {b} ---")
        print(f"CAG: Assignments={results['greedy_assignments'][i]}, "
              f"Satisfaction={results['greedy_satisfaction'][i]:.4f}, "
              f"Time={results['greedy_time'][i]:.4f}s")
        print(f"GT:  Assignments={results['gt_assignments'][i]}, "
              f"Satisfaction={results['gt_satisfaction'][i]:.4f}, "
              f"Time={results['gt_time'][i]:.4f}s")

if __name__ == "__main__":
    # Test with different budget values
    budget_values = [200000, 300000, 400000, 500000]
    
    print("="*70)
    print("Effect of Task Budget on Algorithm Performance")
    print("="*70)
    
    results = run_experiment(budget_values)
    print_results(results)
    plot_results(results)
