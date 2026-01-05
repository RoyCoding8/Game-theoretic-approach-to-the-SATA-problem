from src.common.classes import *
import pandas as pd
from src.probabilistic.monte_carlo import *
from typing import Any

# Collect generated input from csv files

# Budget for each task
df = pd.read_csv(r'data\raw\task_budget.csv')
n=len(df)
budget = [0.0 for _ in range(n+1)]
for _,row in df.iterrows():
    key=row['task']
    value=row['budget']
    budget[int(key)]=float(value)

# Task Location
df = pd.read_csv(r'data\raw\task_location.csv')
task_location = [(0.0,0.0) for _ in range(n+1)]
for _,row in df.iterrows():
    key=row['task']
    task_location[int(key)]=(float(row['latitude']),float(row['longitude']))

# Required Skills for each task
df = pd.read_csv(r'data\raw\task_skills.csv')
task_skills = [[] for _ in range(n+1)]
for _,row in df.iterrows():
    key=row['task']
    value=row['req_skill']
    task_skills[int(key)].append(int(value))

# ----------------------------------------------------------------------------------------

# Worker Location
df = pd.read_csv(r'data\raw\worker_location.csv')
m=len(df)
worker_location = [(0.0,0.0) for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    worker_location[int(key)]=(float(row['latitude']),float(row['longitude']))

# Range of each worker
df = pd.read_csv(r'data\raw\worker_range.csv')
worker_range = [0.0 for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    value=row['range']
    worker_range[int(key)]=float(value)

# Worker Skills
df = pd.read_csv(r'data\raw\worker_skills.csv')
worker_skills = [[] for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    value=row['skill']
    worker_skills[int(key)].append(int(value))

# Worker Cost
df = pd.read_csv(r'data\raw\worker_cost.csv')
worker_cost = [0.0 for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    value=row['cost']
    worker_cost[int(key)]=float(value)

# Tasks that each worker has done before
df = pd.read_csv(r'data\raw\worker_task_history.csv')
task_history = [[] for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    value=row['task']
    task_history[int(key)].append(int(value))

# Worker skills not known fully
df = pd.read_csv(r'data\raw\worker_skills_incomplete.csv')
s = 3        # No of workers with incomplete info about skills
ws_incmp = [[] for _ in range(s+1)]

sub = []
prob_subsets = []

for _,row in df.iterrows():
    key=row['worker']
    probability=row['probability']
    value=row['skill']
    ws_incmp[int(key)].append((float(probability),int(value)))

for i in range(1,len(ws_incmp)):
    tmp = get_subsets(ws_incmp[i])
    sub.append(tmp[0])
    prob_subsets.append(tmp[1])

# all_subsets = generate_all_combinations(sub)
# all_prob = calculate_probabilities(all_subsets,sub,prob_subsets)