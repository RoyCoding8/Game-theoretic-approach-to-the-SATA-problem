from Original import *

# ------------------------Now using synthetic dataset to study the effect of no of tasks---------------------------

# 300 tasks
T,W=[],[]
from Input_t1 import *
from Input_w0 import *
input_tasks(n,T,task_location,task_skills,budget)
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)

print('---------------------300 tasks---------------------')
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_task_greedy.append(len(Asg))
sat_task_greedy.append(s)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_task_gt.append(len(Asg))
sat_task_gt.append(s)

# 400 tasks
T=[]
from Input_t2 import *
from Input_w0 import *
input_tasks(n,T,task_location,task_skills,budget)

print('---------------------400 tasks---------------------')
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_task_greedy.append(len(Asg))
sat_task_greedy.append(s)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_task_gt.append(len(Asg))
sat_task_gt.append(s)

# 500 tasks
T=[]
from Input_t3 import *
from Input_w0 import *
input_tasks(n,T,task_location,task_skills,budget)

print('---------------------500 tasks---------------------')
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_task_greedy.append(len(Asg))
sat_task_greedy.append(s)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_task_gt.append(len(Asg))
sat_task_gt.append(s)

plt.plot([100,300,400,500],assignments_task_greedy,label='CAG')
plt.plot([100,300,400,500],assignments_task_gt,label='GT')
plt.xlabel('No of tasks')
plt.ylabel('No of assignments')
plt.title('No of assignments vs No of tasks')
plt.legend()
plt.show()

plt.plot([100,300,400,500],sat_task_greedy,label='CAG')
plt.plot([100,300,400,500],sat_task_gt,label='GT')
plt.xlabel('No of tasks')
plt.ylabel('Satisfaction score')
plt.title('Satisfaction score vs No of tasks')
plt.legend()
plt.show()
