from Start import *

# --------------------------------- Original (Using 100 tasks and 100 workers) -----------------------------------

# 100 tasks and 100 workers
T,W=[],[]
assignments_task_greedy,assignments_task_gt=[],[]
sat_task_greedy,sat_task_gt=[],[]
assignments_worker_greedy,assignments_worker_gt=[],[]
sat_worker_greedy,sat_worker_gt=[],[]
from Input_t0 import *
from Input_w0 import *
input_tasks(n,T)
input_workers(m,W)

print('---------------------Original---------------------')
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_task_greedy.append(len(Asg))
sat_task_greedy.append(s)
assignments_worker_greedy.append(len(Asg))
sat_worker_greedy.append(s)


Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_task_gt.append(len(Asg))
sat_task_gt.append(s)
assignments_worker_gt.append(len(Asg))
sat_worker_gt.append(s)