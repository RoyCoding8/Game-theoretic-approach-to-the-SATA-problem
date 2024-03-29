from classes import *
import pandas as pd

# Collect generated input from csv files

# Skill_id and Skill_name mapping
df =pd.read_csv(r'.\Generated_Data\Id_and_name\skills_id_name.csv')
s = len(df)         # No of possible skills
skills_tag = ['' for _ in range(s+1)]
for _,row in df.iterrows():
    key=row['skill_id']
    value=row['skill_name']
    skills_tag[key]=value

# Worker_id and Worker_name mapping
df =pd.read_csv(r'.\Generated_Data\Id_and_name\worker_id_name.csv')
m = len(df)         # No of workers
worker_tag = ['' for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker_id']
    value=row['worker_name']
    worker_tag[key]=value

# Task_id and Task_name mapping
df =pd.read_csv(r'.\Generated_Data\Id_and_name\task_id_name.csv')
n = len(df)         # No of tasks
task_tag = ['' for _ in range(n+1)]
for _,row in df.iterrows():
    key=row['task_id']
    value=row['task_name']
    task_tag[key]=value

# ----------------------------------------------------------------------------------------

# Budget for each task
df = pd.read_csv(r'.\Generated_Data\Task_mapping\task_budget.csv')
budget = [0.0 for _ in range(n+1)]
for _,row in df.iterrows():
    key=row['task']
    value=row['budget']
    budget[int(key)]=value

# Task Location
df = pd.read_csv(r'.\Generated_Data\Task_mapping\task_location.csv')
task_location = [(0.0,0.0) for _ in range(n+1)]
for _,row in df.iterrows():
    key=row['task']
    value=(row['longitude'],row['latitude'])
    task_location[int(key)]=value

# Required Skills for each task
df = pd.read_csv(r'.\Generated_Data\Task_mapping\task_skills.csv')
task_skills = [[] for _ in range(n+1)]
for _,row in df.iterrows():
    key=row['task']
    value=row['req_skill']
    task_skills[key].append(value)

# ----------------------------------------------------------------------------------------

# Worker Location
df = pd.read_csv(r'.\Generated_Data\Worker_mapping\worker_location.csv')
worker_location = [(0.0,0.0) for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    value=(row['latitude'],row['longitude']) 
    worker_location[int(key)]=value

# Range of each worker
df = pd.read_csv(r'.\Generated_Data\Worker_mapping\worker_range.csv')
worker_range = [0.0 for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    value=row['range']
    worker_range[int(key)]=value

# Worker Skills
df = pd.read_csv(r'.\Generated_Data\Worker_mapping\worker_skills.csv')
worker_skills = [[] for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    value=row['skill']
    worker_skills[int(key)].append(value)

# Worker Cost
df = pd.read_csv(r'.\Generated_Data\Worker_mapping\worker_cost.csv')
worker_cost = [0.0 for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    value=row['cost']
    worker_cost[int(key)]=value

# Tasks that each worker has done before
df = pd.read_csv(r'.\Generated_Data\Worker_mapping\worker_task_history.csv')
task_history = [[] for _ in range(m+1)]
for _,row in df.iterrows():
    key=row['worker']
    value=row['task']
    task_history[int(key)].append(value)