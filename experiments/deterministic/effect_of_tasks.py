"""
Effect of Number of Tasks on Algorithm Performance
Analyzes how varying the number of tasks affects assignments, satisfaction, and runtime.
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
    m, budget, task_location, task_skills,
    worker_location, worker_range, worker_cost, worker_skills, task_history
)
from data.generators.start import input_tasks, input_workers

def Cal_Sat(Asg):
    """Calculate total satisfaction score for all assignments."""
    return sum(sat(t, [w]) for w, t in Asg)

def run_experiment(task_counts):
    """Run experiments for different task counts."""
    results = {
        'tasks': task_counts,
        'greedy_assignments': [],
        'greedy_satisfaction': [],
        'greedy_time': [],
        'gt_assignments': [],
        'gt_satisfaction': [],
        'gt_time': []
    }
    
    for n_count in task_counts:
        print(f"Running with {n_count} tasks...")
        
        # Create workers (same for all experiments)
        W = []
        input_workers(m, W, worker_location, worker_range, worker_cost, worker_skills, task_history)
        
        # Create subset of tasks
        T = []
        input_tasks(min(n_count, len(task_location)-1), T, task_location, task_skills, budget)
        
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
    tasks = results['tasks']
    
    # Plot 1: Assignments vs Tasks
    plt.figure(figsize=(10, 6))
    plt.plot(tasks, results['greedy_assignments'], 'b-o', label='CAG (Greedy)', linewidth=2)
    plt.plot(tasks, results['gt_assignments'], 'r-s', label='GT', linewidth=2)
    plt.xlabel('Number of Tasks', fontsize=12)
    plt.ylabel('Number of Assignments', fontsize=12)
    plt.title('Effect of Task Count on Number of Assignments', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('experiments/deterministic/tasks_assignments.png', dpi=150)
    plt.show()
    
    # Plot 2: Satisfaction vs Tasks
    plt.figure(figsize=(10, 6))
    plt.plot(tasks, results['greedy_satisfaction'], 'b-o', label='CAG (Greedy)', linewidth=2)
    plt.plot(tasks, results['gt_satisfaction'], 'r-s', label='GT', linewidth=2)
    plt.xlabel('Number of Tasks', fontsize=12)
    plt.ylabel('Total Satisfaction Score', fontsize=12)
    plt.title('Effect of Task Count on Satisfaction Score', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('experiments/deterministic/tasks_satisfaction.png', dpi=150)
    plt.show()
    
    # Plot 3: Time vs Tasks
    plt.figure(figsize=(10, 6))
    plt.plot(tasks, results['greedy_time'], 'b-o', label='CAG (Greedy)', linewidth=2)
    plt.plot(tasks, results['gt_time'], 'r-s', label='GT', linewidth=2)
    plt.xlabel('Number of Tasks', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.title('Effect of Task Count on Running Time', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('experiments/deterministic/tasks_time.png', dpi=150)
    plt.show()

def print_results(results):
    """Print detailed results."""
    print("\n" + "="*70)
    print("RESULTS: Effect of Number of Tasks")
    print("="*70)
    
    for i, t in enumerate(results['tasks']):
        print(f"\n--- {t} Tasks ---")
        print(f"CAG: Assignments={results['greedy_assignments'][i]}, "
              f"Satisfaction={results['greedy_satisfaction'][i]:.4f}, "
              f"Time={results['greedy_time'][i]:.4f}s")
        print(f"GT:  Assignments={results['gt_assignments'][i]}, "
              f"Satisfaction={results['gt_satisfaction'][i]:.4f}, "
              f"Time={results['gt_time'][i]:.4f}s")

if __name__ == "__main__":
    task_counts = [25, 50, 75, 100]
    
    print("="*70)
    print("Effect of Number of Tasks on Algorithm Performance")
    print("="*70)
    
    results = run_experiment(task_counts)
    print_results(results)
    plot_results(results)
