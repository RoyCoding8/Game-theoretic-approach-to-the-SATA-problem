from classes import *
import pandas as pd

def input_skills(x, n):
    if x == 3:
        df = pd.read_csv(r'.\Effect_of_task_skills\3_skills.csv')
    elif x == 4:
        df = pd.read_csv(r'.\Effect_of_task_skills\4_skills.csv')
    elif x == 5:
        df = pd.read_csv(r'.\Effect_of_task_skills\5_skills.csv')
    else:
        df = pd.read_csv(r'.\Effect_of_task_skills\6_skills.csv')
    
    task_skills = [[] for _ in range(n+1)]
    for _,row in df.iterrows():
        key=row['task']
        value=row['req_skill']
        task_skills[key].append(value)