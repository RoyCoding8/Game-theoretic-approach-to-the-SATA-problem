from classes import *
import pandas as pd
from Construct_set import *

# -------------------------------------------------------------------------------------------

# Worker Location
df = pd.read_csv(r'.\Effect_of_workers\200_workers\worker_location.csv')
m = 200
worker_location = [(0.0,0.0) for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    value=(row['latitude'],row['longitude']) 
    worker_location[int(key)]=value

# Range of each worker
df = pd.read_csv(r'.\Effect_of_workers\200_workers\worker_range.csv')
worker_range = [0.0 for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    value=row['range']
    worker_range[int(key)]=value

# Worker Skills
df = pd.read_csv(r'.\Effect_of_workers\200_workers\worker_skills.csv')
worker_skills = [[] for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    value=row['skill']
    worker_skills[int(key)].append(value)

# Worker Cost
df = pd.read_csv(r'.\Effect_of_workers\200_workers\worker_cost.csv')
worker_cost = [0.0 for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    value=row['cost']
    worker_cost[int(key)]=value

# Tasks that each worker has done before
df = pd.read_csv(r'.\Effect_of_workers\200_workers\worker_task_history.csv')
task_history = [[] for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    value=row['task']
    task_history[int(key)].append(value)

# Worker skills not known fully
df = pd.read_csv(r'.\Effect_of_workers\200_workers\worker_skills_incomplete.csv')
s = 3        # No of workers with incomplete info about skills
ws_incmp = [[] for _ in range(s+1)]

sub = []
prob_subsets = []

for _,row in df.iterrows():
    key=row['worker']
    probability=row['probability']
    value=row['skill']
    ws_incmp[int(key)].append((probability,value))

for i in range(1,len(ws_incmp)):
    tmp = get_subsets(ws_incmp[i])
    sub.append(tmp[0])
    prob_subsets.append(tmp[1])

all_subsets = generate_all_combinations(sub)
all_prob = calculate_probabilities(all_subsets,sub,prob_subsets)