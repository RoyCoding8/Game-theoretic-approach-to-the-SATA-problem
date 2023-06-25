from Start import *
import matplotlib.pyplot as plt
import time as tm

# ---------------------- Now using synthetic dataset to study the effect worker range -------------------------

from Input_t0 import *
from Input_w0 import *

T,W=[],[]
worker_range = [6000 for _ in range(m+1)]
assignments_range_greedy,sat_range_greedy,time_range_greedy = [],[],[]
assignments_range_gt,sat_range_gt,time_range_gt = [],[],[]

# worker range = 6000
print('---------------------Worker range = 6000---------------------')
input_tasks(n,T,task_location,task_skills,budget)
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_range_greedy.append(len(Asg))
sat_range_greedy.append(s)
time_range_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('--------------------------------------------------')
assignments_range_gt.append(len(Asg))
sat_range_gt.append(s)
time_range_gt.append(end-start)

# worker range = 7000
print('---------------------Worker range = 7000---------------------')
W=[]
worker_range = [7000 for _ in range(m+1)]
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_range_greedy.append(len(Asg))
sat_range_greedy.append(s)
time_range_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('--------------------------------------------------')
assignments_range_gt.append(len(Asg))
sat_range_gt.append(s)
time_range_gt.append(end-start)

# worker range = 8000
print('---------------------Worker range = 8000---------------------')
W=[]
worker_range = [8000 for _ in range(m+1)]
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_range_greedy.append(len(Asg))
sat_range_greedy.append(s)
time_range_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('--------------------------------------------------')
assignments_range_gt.append(len(Asg))
sat_range_gt.append(s)
time_range_gt.append(end-start)

# worker range = 9000
print('---------------------Worker range = 9000---------------------')
W=[]
worker_range = [9000 for _ in range(m+1)]
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_range_greedy.append(len(Asg))
sat_range_greedy.append(s)
time_range_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('--------------------------------------------------')
assignments_range_gt.append(len(Asg))
sat_range_gt.append(s)
time_range_gt.append(end-start)

# worker range = 10000
print('---------------------Worker range = 10000---------------------')
W=[]
worker_range = [10000 for _ in range(m+1)]
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_range_greedy.append(len(Asg))
sat_range_greedy.append(s)
time_range_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('--------------------------------------------------')
assignments_range_gt.append(len(Asg))
sat_range_gt.append(s)
time_range_gt.append(end-start)

plt.plot([6000,7000,8000,9000,10000],assignments_range_greedy,label='CAG Algorithm')
plt.plot([6000,7000,8000,9000,10000],assignments_range_gt,label='GT Algorithm')
plt.xlabel('Worker Range')
plt.ylabel('No of assignments')
plt.title('Effect of worker range on no of assignments')
plt.legend()
plt.show()

plt.plot([6000,7000,8000,9000,10000],sat_range_greedy,label='CAG Algorithm')
plt.plot([6000,7000,8000,9000,10000],sat_range_gt,label='GT Algorithm')
plt.xlabel('Worker Range')
plt.ylabel('Satisfaction score')
plt.title('Effect of worker range on satisfaction score')
plt.legend()
plt.show()

plt.plot([6000,7000,8000,9000,10000],time_range_greedy,label='CAG Algorithm')
plt.plot([6000,7000,8000,9000,10000],time_range_gt,label='GT Algorithm')
plt.xlabel('Worker Range')
plt.ylabel('Time taken')
plt.title('Effect of worker range on time taken')
plt.legend()
plt.show()