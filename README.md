<b><u><a href="https://drive.google.com/file/d/1aPKLWiZX29fh1D7IKeVYA6wwkCrV10or/view?usp=sharing" target="_blank">The Project Report</a></u></b>

# Satisfaction-Aware Task Assignment Problem

## Table of Contents
- [Introduction](#introduction)
- [Problem Description](#problem-description)
- [Approaches](#approaches)
- [Comparison Metrics](#comparison-metrics)
- [Installation](#installation)
- [Usage](#usage)

## Introduction
The Task-Worker Assignment Optimization project aims to solve the task-worker assignment problem by maximizing the overall satisfaction score. The problem involves assigning workers to tasks based on various constraints such as location, skills, range, budget, and travel costs. This repository provides implementations of two approaches, Greedy and Game-Theoretic, to address the problem along with evaluation metrics to compare the performance of the algorithms.

In the 'Complete info' part, we use deterministic skills for all workers whereas in the 'Incomplete info' part, we use probabilistic skills for some of the workers and some more corresponding evauation metrics.

## Problem Description
The Satisfaction-Aware Task Assignment problem requires finding the optimal assignment of task-worker pairs that maximizes the expected overall satisfaction score. Each worker is defined by a 4-tuple (L, K, R, v), representing location, skill set, range, and unit cost of travel. Similarly, each task is represented by a 4-tuple (L, K, B, D), representing location, required skill set, budget, and expiry date. The problem is subject to constraints such as working range, skill compatibility and budget constraints.

## Approaches
1. **Greedy Approach**: The Greedy algorithm assigns workers to tasks based on satisfaction score increments. Conflicts between workers are resolved to maximize satisfaction increment. Unassigned workers are considered in singleton worker sets, and the highest satisfaction score tasks are prioritized. After this, even if some workers are not assigned, we use them for further processing in other algorithms.
2. **Game-Theoretic Approach**: The Game-Theoretic approach builds upon the Greedy algorithm's initial assignment. The problem is modeled as a game, and the optimal strategy for each worker is determined using Nash Equilibrium. Unassigned workers are swapped with assigned workers only if the satisfaction score is improved until a Nash Equilibrium is reached.

## Comparison Metrics
The performance of the Greedy and Game-Theoretic approaches is compared using the following metrics:
- Number of assigned workers: Indicates the utilization of workers in the assignment process.
- Total satisfaction score: Represents the expected overall satisfaction achieved by the assignment.
- Time taken: Measures the total execution time for running both the Greedy and Game-Theoretic algorithms.

## Installation
1. Clone the repository or Code → Download zip.
2. Extract the folder if downloaded zip, and navigate to it in file explorer.
3. Make sure that python3 is installed on your system. After installing python3, run the following commands in terminal to install the required libraries:
```
pip install matplotlib
pip install pandas
```

## Usage
1. Navigate to 'Incomplete info' or 'Complete info' folder as per requirement.
2. Open terminal in that folder.
3. Run the following command to execute the program:
    ```
    python <file_name>.py
    ```
    where ```<file_name>``` is to be chosen as per requirement. For example, to view the assignment in the complete info version, use ```python main.py```.
4. The details for the evaluation metrics can be found in the ```main.py``` as comments.
