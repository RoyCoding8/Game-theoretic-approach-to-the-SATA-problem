from classes import *
import pandas as pd

# -------------------------------------------------------------------------------------------

# Worker Location
df = pd.read_csv(r'.\Effect_of_workers\500_workers\worker_location.csv')
m=len(df)
worker_location = [(0.0,0.0)]*(m+1)
for _,row in df.iterrows():
    key=row['worker']
    value=(row['latitude'],row['longitude']) 
    worker_location[int(key)]=value

# Worker Skills
df = pd.read_csv(r'.\Effect_of_workers\500_workers\worker_skills.csv')
worker_skills = [[]]*(m+1)
for _,row in df.iterrows():
    key=row['worker']
    value=row['skill']
    worker_skills[int(key)].append(value)

# Worker Cost
df = pd.read_csv(r'.\Effect_of_workers\500_workers\worker_cost.csv')
worker_cost = [0.0]*(m+1)
for _,row in df.iterrows():
    key=row['worker']
    value=row['cost']
    worker_cost[int(key)]=value

# Tasks that each worker has done before
df = pd.read_csv(r'.\Effect_of_workers\500_workers\worker_task_history.csv')
task_history = [[]]*(m+1)
for _,row in df.iterrows():
    key=row['worker']
    value=row['task']
    task_history[int(key)].append(value)