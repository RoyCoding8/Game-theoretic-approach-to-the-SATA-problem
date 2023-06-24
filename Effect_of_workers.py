from Original import *

# ------------------------Now using synthetic dataset to study the effect of no of workers----------------------------
# 300 workers
T,W=[],[]
from Input_w1 import *
from Input_t0 import *
input_tasks(n,T)
input_workers(m,W)

print('---------------------300 workers---------------------')
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_worker_greedy.append(len(Asg))
sat_worker_greedy.append(s)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_worker_gt.append(len(Asg))
sat_worker_gt.append(s)

# 400 workers
T,W=[],[]
from Input_w2 import *
from Input_t0 import *
input_tasks(n,T)
input_workers(m,W)

print('---------------------400 workers---------------------')
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_worker_greedy.append(len(Asg))
sat_worker_greedy.append(s)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_worker_gt.append(len(Asg))
sat_worker_gt.append(s)

# 500 workers
T,W=[],[]
from Input_w3 import *
from Input_t0 import *
input_tasks(n,T)
input_workers(m,W)

print('---------------------500 workers---------------------')
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_worker_greedy.append(len(Asg))
sat_worker_greedy.append(s)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_worker_gt.append(len(Asg))
sat_worker_gt.append(s)

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
