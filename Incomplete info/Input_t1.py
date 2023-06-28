from classes import *
import pandas as pd
from Construct_set import *

# -------------------------------------------------------------------------------------------

# Budget for each task
df = pd.read_csv(r'.\Effect_of_tasks\150_tasks\task_budget.csv')
n=len(df)
budget = [0.0 for _ in range(n+1)]
for _,row in df.iterrows():
    key=row['task']
    value=row['budget']
    budget[int(key)]=value

# Task Location
df = pd.read_csv(r'.\Effect_of_tasks\150_tasks\task_location.csv')
task_location = [(0.0,0.0) for _ in range(n+1)]
for _,row in df.iterrows():
    key=row['task']
    value=(row['longitude'],row['latitude'])
    task_location[int(key)]=value

# Required Skills for each task
df = pd.read_csv(r'.\Effect_of_tasks\150_tasks\task_skills.csv')
task_skills = [[] for _ in range(n+1)]
for _,row in df.iterrows():
    key=row['task']
    value=row['req_skill']
    task_skills[key].append(value)

# Worker skills not known fully
df = pd.read_csv(r'.\Generated_Data\Worker_mapping\worker_skills_incomplete.csv')
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
# -------------------------------------------------------------------------------------------