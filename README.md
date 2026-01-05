<b><u><a href="https://drive.google.com/file/d/1aPKLWiZX29fh1D7IKeVYA6wwkCrV10or/view?usp=sharing" target="_blank">The Project Report</a></u></b>

# Satisfaction-Aware Task Assignment Problem (SATA)

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Approaches](#approaches)
- [Installation](#installation)
- [Usage](#usage)

## Introduction
The Task-Worker Assignment Optimization project aims to solve the task-worker assignment problem by maximizing the overall satisfaction score. The problem involves assigning workers to tasks based on various constraints like location (spatial), skills, range, budget, and travel costs. 

This repository implements two core approaches: **Conflict-Aware Greedy (CAG)** and **Game-Theoretic (GT)** algorithm with threshold stop optimization. It handles both **deterministic** scenarios (complete worker info) and **probabilistic** scenarios (incomplete worker skill info via Monte Carlo sampling).

**Key Features:**
- **Modular Codebase**: Clean structure with separate packages for algorithms, utilities, and data.
- **Monte Carlo Simulation**: Scalable probabilistic calculation (replaces exponential brute-force).
- **Full Nash Equilibrium**: GT algorithm supports Join, Switch, and Leave moves.
- **Comprehensive Tests**: Extensive test suite for verification.
- **Visualization Scripts**: Ready-to-run experiment scripts with matplotlib plotting.

## Project Structure

```
Game-theoretic-approach-to-the-SATA-problem/
├── src/                            # Core Library
│   ├── common/                     # Shared utilities
│   │   ├── classes.py              # worker, task class definitions
│   │   ├── distance.py             # Haversine distance calculation
│   │   └── utils.py                # Satisfaction formulas, constraint checks
│   ├── algorithms/                 # Assignment algorithms
│   │   ├── greedy.py               # Conflict-Aware Greedy (CAG)
│   │   └── gt.py                   # Game Theoretic (GT) algorithm
│   └── probabilistic/              # Uncertainty handling
│       └── monte_carlo.py          # Skill sampling functions
│
├── data/                           # Input Data
│   ├── generators/                 # Data loading scripts
│   │   ├── gen_input.py            # Main CSV loader
│   │   └── start.py                # Helper functions
│   └── raw/                        # CSV files (12 files)
│       ├── task_budget.csv
│       ├── task_location.csv
│       ├── task_skills.csv
│       ├── worker_location.csv
│       ├── worker_range.csv
│       ├── worker_skills.csv
│       ├── worker_cost.csv
│       ├── worker_task_history.csv
│       └── worker_skills_incomplete.csv
│
├── experiments/                    # Experiment Scripts
│   ├── deterministic/              # Complete info experiments
│   │   ├── effect_of_budget.py
│   │   ├── effect_of_workers.py
│   │   ├── effect_of_tasks.py
│   │   └── effect_of_ranges.py
│   ├── probabilistic/              # Incomplete info experiments
│   │   ├── main.py                 # Monte Carlo entry point
│   │   └── effect_of_monte_carlo.py
│   └── run_all.py                  # Master script to run all experiments
│
├── tests/                          # Test Suite
│   └── test_sanity.py              # Quick sanity check
└── README.md                       # This file
```

## Approaches

### 1. Conflict-Aware Greedy (CAG)
Iteratively assigns workers to tasks based on maximum satisfaction increment. Resolves conflicts when multiple tasks compete for the same worker by comparing satisfaction losses.

### 2. Game-Theoretic (GT) Algorithm
Builds upon CAG's initial assignment. Workers proactively optimize their assignments through:
- **Join**: Unassigned worker joins a task
- **Switch**: Worker moves from one task to another
- **Leave**: Worker becomes unassigned

The process continues until a **Nash Equilibrium** is reached (no worker can improve by unilaterally changing).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Game-theoretic-approach-to-the-SATA-problem.git
   cd Game-theoretic-approach-to-the-SATA-problem
   ```

2. Ensure **Python 3.8+** is installed.

3. Install dependencies:
   ```bash
   pip install pandas matplotlib
   ```

## Usage

### Run Tests
```bash
# Comprehensive test suite
python tests/test.py

# Quick sanity check
python tests/test_sanity.py
```

### Run Individual Experiments
```bash
# Effect of budget on performance
python experiments/deterministic/effect_of_budget.py

# Effect of worker count
python experiments/deterministic/effect_of_workers.py

# Monte Carlo probabilistic experiment
python experiments/probabilistic/effect_of_monte_carlo.py
```

### Run All Experiments
```bash
python experiments/run_all.py
```
This generates plots saved as PNG files in the respective experiment folders.

### Probabilistic Main Entry Point
```bash
python experiments/probabilistic/main.py
```
Runs 500 Monte Carlo simulations and outputs expected satisfaction scores.

## Output
Each experiment script:
- Prints detailed results to console
- Generates 3 matplotlib plots:
  - Assignments vs. Variable
  - Satisfaction Score vs. Variable
  - Runtime vs. Variable
- Saves plots as PNG files in the experiment folder
