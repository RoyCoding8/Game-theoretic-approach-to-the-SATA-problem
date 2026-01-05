import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

print("SATA Experiments Runner")
print("=" * 50)

print("\n[1/5] Budget...")
from experiments.deterministic.effect_of_budget import run as run_budget
run_budget([200000, 300000, 400000, 500000])

print("\n[2/5] Workers...")
from experiments.deterministic.effect_of_workers import run as run_workers
run_workers([25, 50, 75, 100])

print("\n[3/5] Tasks...")
from experiments.deterministic.effect_of_tasks import run as run_tasks
run_tasks([25, 50, 75, 100])

print("\n[4/5] Ranges...")
from experiments.deterministic.effect_of_ranges import run as run_ranges
run_ranges([25, 50, 75, 100])

print("\n[5/5] Monte Carlo...")
from experiments.probabilistic.effect_of_monte_carlo import run as run_mc
run_mc([10, 50, 100])

print("\nDone! Plots saved in experiments/")
