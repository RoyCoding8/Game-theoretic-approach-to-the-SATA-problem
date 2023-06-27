from Original import *
import matplotlib.pyplot as plt
import time as tm

# ------------------------Now using synthetic dataset to study the effect of no of workers----------------------------
# 300 workers
T,W=[],[]
from Input_w1 import *
from Input_t0 import *
input_tasks(n,T,task_location,task_skills,budget)
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)

print('---------------------300 workers---------------------')
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_worker_greedy.append(len(Asg))
sat_worker_greedy.append(s)
time_worker_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('--------------------------------------------------')
assignments_worker_gt.append(len(Asg))
sat_worker_gt.append(s)
time_worker_gt.append(end-start)

# 400 workers
W=[]
from Input_w2 import *
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)

print('---------------------400 workers---------------------')
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_worker_greedy.append(len(Asg))
sat_worker_greedy.append(s)
time_worker_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('--------------------------------------------------')
assignments_worker_gt.append(len(Asg))
sat_worker_gt.append(s)
time_worker_gt.append(end-start)

# 500 workers
W=[]
from Input_w3 import *
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)

print('---------------------500 workers---------------------')
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_worker_greedy.append(len(Asg))
sat_worker_greedy.append(s)
time_worker_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('--------------------------------------------------')
assignments_worker_gt.append(len(Asg))
sat_worker_gt.append(s)
time_worker_gt.append(end-start)

plt.plot([100,300,400,500],assignments_worker_greedy,label='CAG')
plt.plot([100,300,400,500],assignments_worker_gt,label='GT')
plt.xlabel('No of workers')
plt.ylabel('No of assignments')
plt.title('No of assignments vs No of workers')
plt.legend()
plt.show()

plt.plot([100,300,400,500],sat_worker_greedy,label='CAG')
plt.plot([100,300,400,500],sat_worker_gt,label='GT')
plt.xlabel('No of workers')
plt.ylabel('Satisfaction score')
plt.title('Satisfaction score vs No of workers')
plt.legend()
plt.show()

plt.plot([100,300,400,500],time_worker_greedy,label='CAG')
plt.plot([100,300,400,500],time_worker_gt,label='GT')
plt.xlabel('No of workers')
plt.ylabel('Time taken')
plt.title('Time taken vs No of workers')
plt.legend()
plt.show()