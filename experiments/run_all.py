"""
Run All Experiments
Master script to run all deterministic and probabilistic experiments.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

print("="*70)
print("SATA Experiments Runner")
print("="*70)

print("\n[1/5] Effect of Budget...")
from experiments.deterministic.effect_of_budget import run_experiment as run_budget
budget_results = run_budget([200000, 300000, 400000, 500000])

print("\n[2/5] Effect of Workers...")
from experiments.deterministic.effect_of_workers import run_experiment as run_workers
worker_results = run_workers([25, 50, 75, 100])

print("\n[3/5] Effect of Tasks...")
from experiments.deterministic.effect_of_tasks import run_experiment as run_tasks
task_results = run_tasks([25, 50, 75, 100])

print("\n[4/5] Effect of Ranges...")
from experiments.deterministic.effect_of_ranges import run_experiment as run_ranges
range_results = run_ranges([0.5, 1.0, 1.5, 2.0])

print("\n[5/5] Monte Carlo Probabilistic...")
from experiments.probabilistic.effect_of_monte_carlo import run_monte_carlo
mc_results = run_monte_carlo([10, 50, 100])

print("\n" + "="*70)
print("ALL EXPERIMENTS COMPLETED!")
print("="*70)
print("\nPlots saved in:")
print("  - experiments/deterministic/")
print("  - experiments/probabilistic/")
