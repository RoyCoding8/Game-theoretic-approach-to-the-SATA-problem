from GT import *
from Input import *
from Output import *

T,W=[],[]

# Input (can be changed later to file based input)
n = int(input()) # no of tasks
for i in range(n):
    T.append(input_tasks(i+1))
m = int(input()) # no of workers
for i in range(m):
    W.append(input_workers(i+1))

# Output
Asg=GT_algo(T,W)
Output(Asg)