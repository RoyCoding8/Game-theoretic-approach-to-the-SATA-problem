from GT import *
from Gen_input import *
from Output import *
from Calculate_Sat import *
import time as tm

def input_tasks(n,T,task_location,task_skills,budget):
    for i in range(1,n+1):

        # Create the task object and put it in task set
        obj=task(i,task_location[i][0],task_location[i][1],task_skills[i],budget[i],POS_INF)
        T.append(obj)

def input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history):
    for i in range(1,m+1):

        # Create the worker object and put it in worker set
        obj=worker(i,worker_location[i][0],worker_location[i][1],worker_range[i],worker_cost[i],worker_skills[i],task_history[i])
        W.append(obj)