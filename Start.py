from GT import *
from Gen_input import *
from Output import *
from Calculate_Sat import *
import matplotlib.pyplot as plt

def input_tasks(n,T:list[task]):
    for i in range(n):

        # Create the task object and put it in task set
        obj=task(i+1,task_location[i+1][0],task_location[i+1][1],task_skills[i+1],budget[i+1],POS_INF)
        T.append(obj)

def input_workers(m,W):
    for i in range(m):

        # Create the worker object and put it in worker set
        obj=worker(i+1,worker_location[i+1][0],worker_location[i+1][1],POS_INF,worker_cost[i+1],worker_skills[i+1],task_history[i+1])
        W.append(obj)
