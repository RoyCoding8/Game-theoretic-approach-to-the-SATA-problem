from Start import *
import time as tm

# --------------------------------- Original (Using 100 tasks and 100 workers) -----------------------------------

# 100 tasks and 100 workers
T,W=[],[]
assignments_task_greedy,assignments_task_gt=[],[]
sat_task_greedy,sat_task_gt=[],[]
time_task_greedy,time_task_gt=[],[]
assignments_worker_greedy,assignments_worker_gt=[],[]
sat_worker_greedy,sat_worker_gt=[],[]
time_worker_greedy,time_worker_gt=[],[]
from Input_t0 import *
from Input_w0 import *
input_tasks(n,T,task_location,task_skills,budget)
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)

print('---------------------Original---------------------')
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_task_greedy.append(len(Asg))
sat_task_greedy.append(s)
assignments_worker_greedy.append(len(Asg))
sat_worker_greedy.append(s)
time_task_greedy.append(end-start)
time_worker_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('\nNo of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('-----------------------------------------------------')
assignments_task_gt.append(len(Asg))
sat_task_gt.append(s)
assignments_worker_gt.append(len(Asg))
sat_worker_gt.append(s)
time_task_gt.append(end-start)
time_worker_gt.append(end-start)