"""
Monte Carlo Probabilistic Experiment Visualization
Analyzes algorithm performance under uncertainty using Monte Carlo sampling.
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
from src.probabilistic.monte_carlo import sample_skills, get_subsets
from data.generators.gen_input import (
    n, m, budget, task_location, task_skills,
    worker_location, worker_range, worker_cost, worker_skills, task_history, ws_incmp
)
from data.generators.start import input_tasks, input_workers

def Cal_Sat(Asg):
    """Calculate total satisfaction score for all assignments."""
    return sum(sat(t, [w]) for w, t in Asg)

def run_monte_carlo(num_samples_list):
    """Run Monte Carlo experiments with different sample sizes."""
    results = {
        'samples': num_samples_list,
        'greedy_assignments': [],
        'greedy_satisfaction': [],
        'gt_assignments': [],
        'gt_satisfaction': [],
        'time': []
    }
    
    # Create tasks once
    T = []
    input_tasks(n, T, task_location, task_skills, budget)
    
    for num_samples in num_samples_list:
        print(f"Running Monte Carlo with {num_samples} samples...")
        
        asg_greedy_total = 0
        sat_greedy_total = 0
        asg_gt_total = 0
        sat_gt_total = 0
        
        start = tm.time()
        
        for _ in range(num_samples):
            # Sample skills for uncertain workers
            sampled = sample_skills(ws_incmp)
            
            # Create copy of worker_skills and update with sampled values
            current_skills = worker_skills.copy()
            for worker_idx, skills in sampled.items():
                current_skills[worker_idx] = skills
            
            # Create workers with current skills
            W = []
            input_workers(m, W, worker_location, worker_range, worker_cost, current_skills, task_history)
            
            # Run Greedy
            Asg_greedy, _ = greedy(T, W)
            asg_greedy_total += len(Asg_greedy)
            sat_greedy_total += Cal_Sat(Asg_greedy)
            
            # Run GT
            Asg_gt = GT_algo(T, W)
            asg_gt_total += len(Asg_gt)
            sat_gt_total += Cal_Sat(Asg_gt)
        
        end = tm.time()
        
        # Average results
        results['greedy_assignments'].append(asg_greedy_total / num_samples)
        results['greedy_satisfaction'].append(sat_greedy_total / num_samples)
        results['gt_assignments'].append(asg_gt_total / num_samples)
        results['gt_satisfaction'].append(sat_gt_total / num_samples)
        results['time'].append(end - start)
    
    return results

def plot_results(results):
    """Generate visualization plots."""
    samples = results['samples']
    
    # Plot 1: Average Assignments vs Sample Size
    plt.figure(figsize=(10, 6))
    plt.plot(samples, results['greedy_assignments'], 'b-o', label='CAG (Greedy)', linewidth=2)
    plt.plot(samples, results['gt_assignments'], 'r-s', label='GT', linewidth=2)
    plt.xlabel('Number of Monte Carlo Samples', fontsize=12)
    plt.ylabel('Average Number of Assignments', fontsize=12)
    plt.title('Monte Carlo: Average Assignments vs Sample Size', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('experiments/probabilistic/mc_assignments.png', dpi=150)
    plt.show()
    
    # Plot 2: Average Satisfaction vs Sample Size
    plt.figure(figsize=(10, 6))
    plt.plot(samples, results['greedy_satisfaction'], 'b-o', label='CAG (Greedy)', linewidth=2)
    plt.plot(samples, results['gt_satisfaction'], 'r-s', label='GT', linewidth=2)
    plt.xlabel('Number of Monte Carlo Samples', fontsize=12)
    plt.ylabel('Average Satisfaction Score', fontsize=12)
    plt.title('Monte Carlo: Average Satisfaction vs Sample Size', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('experiments/probabilistic/mc_satisfaction.png', dpi=150)
    plt.show()
    
    # Plot 3: Total Time vs Sample Size
    plt.figure(figsize=(10, 6))
    plt.plot(samples, results['time'], 'g-^', label='Total Time', linewidth=2)
    plt.xlabel('Number of Monte Carlo Samples', fontsize=12)
    plt.ylabel('Total Time (seconds)', fontsize=12)
    plt.title('Monte Carlo: Computation Time vs Sample Size', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('experiments/probabilistic/mc_time.png', dpi=150)
    plt.show()

def print_results(results):
    """Print detailed results."""
    print("\n" + "="*70)
    print("RESULTS: Monte Carlo Probabilistic Experiment")
    print("="*70)
    
    for i, s in enumerate(results['samples']):
        print(f"\n--- {s} Samples ---")
        print(f"CAG: Avg Assignments={results['greedy_assignments'][i]:.2f}, "
              f"Avg Satisfaction={results['greedy_satisfaction'][i]:.4f}")
        print(f"GT:  Avg Assignments={results['gt_assignments'][i]:.2f}, "
              f"Avg Satisfaction={results['gt_satisfaction'][i]:.4f}")
        print(f"Total Time: {results['time'][i]:.2f}s")

if __name__ == "__main__":
    num_samples_list = [10, 50, 100, 200]
    
    print("="*70)
    print("Monte Carlo Probabilistic Experiment")
    print("="*70)
    
    results = run_monte_carlo(num_samples_list)
    print_results(results)
    plot_results(results)
