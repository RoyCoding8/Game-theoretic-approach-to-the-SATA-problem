from GT import *
from Gen_input import *
from Output import *

def input_tasks(n,T:list[task]):
    for i in range(n):

        # Create the task object and put it in task set
        obj=task(i+1,task_location[i+1][0],task_location[i+1][1],task_skills[i+1],budget[i+1],POS_INF)
        T.append(obj)

def input_workers(m,W):
    for i in range(m):

        # Create the worker object and put it in worker set
        obj=worker(i+1,worker_location[i+1][0],worker_location[i+1][1],0,worker_cost[i+1],worker_skills[i+1],task_history[i+1])
        W.append(obj)

T,W=[],[]

# Create the task set using the input
input_tasks(n,T)

# Create the worker set using the input
input_workers(m,W)

# Get the assignment
Asg=GT_algo(T,W)

# Print the assignment
Output(Asg)
