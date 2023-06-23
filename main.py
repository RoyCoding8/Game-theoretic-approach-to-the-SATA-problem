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
        obj=worker(i+1,worker_location[i+1][0],worker_location[i+1][1],POS_INF,worker_cost[i+1],worker_skills[i+1],task_history[i+1])
        W.append(obj)

T,W=[],[]

# Create the task set using the input
input_tasks(n,T)

# Create the worker set using the input
input_workers(m,W)

# Running the program

print('--------------------------------------------------')
print('Greedy algorithm assignment:\n')
Asg=greedy(T,W)[0]

# Print the assignment
Output(Asg)
print('--------------------------------------------------')

print('GT algorithm assignment:\n')
Asg=GT_algo(T,W)

# Print the assignment
Output(Asg)
print('--------------------------------------------------')

# ------------------------Now using synthetic dataset to study the effect of no of tasks---------------------------

# 300 tasks
T,W=[],[]
from Input_t1 import *
from Input_w0 import *
input_tasks(n,T)
input_workers(m,W)

print('---------------------300 tasks---------------------')
Asg=greedy(T,W)[0]
print('Greedy algorithm assignment:',len(Asg))

Asg=GT_algo(T,W)
print('GT algorithm assignment:',len(Asg))
print('--------------------------------------------------')

# 400 tasks
T,W=[],[]
from Input_t2 import *
from Input_w0 import *
input_tasks(n,T)
input_workers(m,W)

print('---------------------400 tasks---------------------')
Asg=greedy(T,W)[0]
print('Greedy algorithm assignment:',len(Asg))

Asg=GT_algo(T,W)
print('GT algorithm assignment:',len(Asg))
print('--------------------------------------------------')

# 500 tasks
T,W=[],[]
from Input_t3 import *
from Input_w0 import *
input_tasks(n,T)
input_workers(m,W)

print('---------------------500 tasks---------------------')
Asg=greedy(T,W)[0]
print('Greedy algorithm assignment:',len(Asg))

Asg=GT_algo(T,W)
print('GT algorithm assignment:',len(Asg))
print('--------------------------------------------------')

# ------------------------Now using synthetic dataset to study the effect of no of workers----------------------------
# 300 workers
T,W=[],[]
from Input_w1 import *
from Input_t0 import *
input_tasks(n,T)
input_workers(m,W)

print('---------------------300 workers---------------------')
Asg=greedy(T,W)[0]
print('Greedy algorithm assignment:',len(Asg))

Asg=GT_algo(T,W)
print('GT algorithm assignment:',len(Asg))
print('--------------------------------------------------')

# 400 workers
T,W=[],[]
from Input_w2 import *
from Input_t0 import *
input_tasks(n,T)
input_workers(m,W)

print('---------------------400 workers---------------------')
Asg=greedy(T,W)[0]
print('Greedy algorithm assignment:',len(Asg))

Asg=GT_algo(T,W)
print('GT algorithm assignment:',len(Asg))
print('--------------------------------------------------')

# 500 workers
T,W=[],[]
from Input_w3 import *
from Input_t0 import *
input_tasks(n,T)
input_workers(m,W)

print('---------------------500 workers---------------------')
Asg=greedy(T,W)[0]
print('Greedy algorithm assignment:',len(Asg))

Asg=GT_algo(T,W)
print('GT algorithm assignment:',len(Asg))
print('--------------------------------------------------')