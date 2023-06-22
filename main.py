from GT import *
from Gen_input import *
from Output import *

T,W=[],[]

def input_tasks(n,T):
    for i in range(n):
        obj=task(i+1,task_location[i+1][0],task_location[i+1][1],task_skills[i+1],budget[i+1],POS_INF)
        T.append(obj)

def input_workers(m,W):
    for i in range(m):
        obj=worker(i+1,worker_location[i+1][0],worker_location[i+1][1],0,worker_cost[i+1],worker_skills[i+1],task_history[i+1])
        W.append(obj)

# No of tasks
n = 100
input_tasks(n,T)

# No of workers
m = 100
input_workers(m,W)

# Output
Asg=GT_algo(T,W)
Output(Asg)