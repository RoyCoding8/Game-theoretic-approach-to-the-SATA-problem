from Start import *
import matplotlib.pyplot as plt
import time as tm

# ----------------------Now using synthetic dataset to study the effect worker cost-------------------------

from Input_t0 import *
from Input_w0 import *

T,W=[],[]
worker_cost = [5 for _ in range(m+1)]
assignments_cost_greedy,sat_cost_greedy,time_cost_greedy = [],[],[]
assignments_cost_gt,sat_cost_gt,time_cost_gt = [],[],[]

# worker cost = 5
print('---------------------Worker cost = 5---------------------')
input_tasks(n,T,task_location,task_skills,budget)
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time() 
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_cost_greedy.append(len(Asg))
sat_cost_greedy.append(s)
time_cost_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('\nNo of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('----------------------------------------------------------')
assignments_cost_gt.append(len(Asg))
sat_cost_gt.append(s)
time_cost_gt.append(end-start)

# worker cost = 7
print('---------------------Worker cost = 7---------------------')
W=[]
worker_cost = [7 for _ in range(m+1)]
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_cost_greedy.append(len(Asg))
sat_cost_greedy.append(s)
time_cost_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('\nNo of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('----------------------------------------------------------')
assignments_cost_gt.append(len(Asg))
sat_cost_gt.append(s)
time_cost_gt.append(end-start)

# worker cost = 8
print('---------------------Worker cost = 8---------------------')
W=[]
worker_cost = [8 for _ in range(m+1)]
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_cost_greedy.append(len(Asg))
sat_cost_greedy.append(s)
time_cost_greedy.append(end-start)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('\nNo of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('----------------------------------------------------------')
assignments_cost_gt.append(len(Asg))
sat_cost_gt.append(s)
time_cost_gt.append(end-start)

# worker cost = 10
print('---------------------Worker cost = 10---------------------')
W=[]
worker_cost = [10 for _ in range(m+1)]
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_cost_greedy.append(len(Asg))
sat_cost_greedy.append(s)
time_cost_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('\nNo of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('----------------------------------------------------------')
assignments_cost_gt.append(len(Asg))
sat_cost_gt.append(s)
time_cost_gt.append(end-start)

plt.plot([5,7,8,10],assignments_cost_greedy,label='CAG')
plt.plot([5,7,8,10],assignments_cost_gt,label='GT')
plt.xlabel('Worker cost')
plt.ylabel('No of assignments')
plt.title('No of assignments vs Worker cost')
plt.legend()
plt.show()

plt.plot([5,7,8,10],sat_cost_greedy,label='CAG')
plt.plot([5,7,8,10],sat_cost_gt,label='GT')
plt.xlabel('Worker cost')
plt.ylabel('Satisfaction score')
plt.title('Satisfaction score vs Worker cost')
plt.legend()
plt.show()

plt.plot([5,7,8,10],time_cost_greedy,label='CAG')
plt.plot([5,7,8,10],time_cost_gt,label='GT')
plt.xlabel('Worker cost')
plt.ylabel('Time taken')
plt.title('Time taken vs Worker cost')
plt.legend()
plt.show()