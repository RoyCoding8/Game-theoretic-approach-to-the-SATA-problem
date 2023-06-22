from classes import *
import pandas as pd

n, m = 100, 100
s = 110
# Skill_id and Skill_name mapping
df =pd.read_csv(r'.\Generated_Data\Id_and_name\skills_id_name.csv')
skills_tag = ['']*(s+1)
for _,row in df.iterrows():
    key=row['skill_id']
    value=row['skill_name']
    skills_tag[key]=value

# Worker_id and Worker_name mapping
df =pd.read_csv(r'.\Generated_Data\Id_and_name\worker_id_name.csv')
worker_tag = ['']*(m+1)
for _,row in df.iterrows():
    key=row['worker_id']
    value=row['worker_name']
    worker_tag[key]=value

# Task_id and Task_name mapping
df =pd.read_csv(r'.\Generated_Data\Id_and_name\task_id_name.csv')
task_tag = ['']*(n+1)
for _,row in df.iterrows():
    key=row['task_id']
    value=row['task_name']
    task_tag[key]=value

# ----------------------------------------------------------------------------------------

# Budget for each task
df = pd.read_csv(r'.\Generated_Data\Task_mapping\task_budget.csv')
budget = [0.0]*(n+1)
for _,row in df.iterrows():
    key=row['task']
    value=row['budget']
    budget[int(key)]=value

# Task Location
df = pd.read_csv(r'.\Generated_Data\Task_mapping\task_location.csv')
task_location = [(0.0,0.0)]*(n+1)
for _,row in df.iterrows():
    key=row['task']
    value=(row['longitude'],row['latitude'])
    task_location[int(key)]=value

# Required Skills for each task
df = pd.read_csv(r'.\Generated_Data\Task_mapping\task_skills.csv')
task_skills = [[]]*(n+1)
for _,row in df.iterrows():
    key=row['task']
    value=row['req_skill']
    task_skills[key].append(value)

# ----------------------------------------------------------------------------------------

# Worker Location
df = pd.read_csv(r'.\Generated_Data\Worker_mapping\worker_location.csv')
worker_location = [(0.0,0.0)]*(m+1)
for _,row in df.iterrows():
    key=row['worker']
    value=(row['latitude'],row['longitude']) 
    worker_location[int(key)]=value

# Worker Skills
df = pd.read_csv(r'.\Generated_Data\Worker_mapping\worker_skills.csv')
worker_skills = [[]]*(m+1)
for _,row in df.iterrows():
    key=row['worker']
    value=row['skill']
    worker_skills[int(key)].append(value)

# Worker Cost
df = pd.read_csv(r'.\Generated_Data\Worker_mapping\worker_cost.csv')
worker_cost = [0.0]*(m+1)
for _,row in df.iterrows():
    key=row['worker']
    value=row['cost']
    worker_cost[int(key)]=value

# Tasks that each worker has done before
df = pd.read_csv(r'.\Generated_Data\Worker_mapping\worker_task_history.csv')
task_history = [[]]*(m+1)
for _,row in df.iterrows():
    key=row['worker']
    value=row['task']
    task_history[int(key)].append(value)