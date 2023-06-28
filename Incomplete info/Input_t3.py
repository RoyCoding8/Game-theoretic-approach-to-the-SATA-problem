from classes import *
import pandas as pd

# -------------------------------------------------------------------------------------------

# Budget for each task
df = pd.read_csv(r'.\Effect_of_tasks\250_tasks\task_budget.csv')
n=len(df)
budget = [0.0 for _ in range(n+1)]
for _,row in df.iterrows():
    key=row['task']
    value=row['budget']
    budget[int(key)]=value

# Task Location
df = pd.read_csv(r'.\Effect_of_tasks\250_tasks\task_location.csv')
task_location = [(0.0,0.0) for _ in range(n+1)]
for _,row in df.iterrows():
    key=row['task']
    value=(row['longitude'],row['latitude'])
    task_location[int(key)]=value

# Required Skills for each task
df = pd.read_csv(r'.\Effect_of_tasks\250_tasks\task_skills.csv')
task_skills = [[] for _ in range(n+1)]
for _,row in df.iterrows():
    key=row['task']
    value=row['req_skill']
    task_skills[key].append(value)

# -------------------------------------------------------------------------------------------