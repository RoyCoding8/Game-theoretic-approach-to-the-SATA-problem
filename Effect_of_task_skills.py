from Start import *
import matplotlib.pyplot as plt
import time as tm

# ---------------------Now using synthetic dataset to study the effect of complexity of tasks---------------------

from Input_t0 import *
from Input_w0 import *
from Input_skill import *
W=[]
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)

assignments_skill_greedy,sat_skill_greedy,time_skill_greedy = [],[],[]
assignments_skill_gt,sat_skill_gt,time_skill_gt = [],[],[]

# no of task skills = 3
print('---------------------No of task skills = 3---------------------')
T=[]
input_skills(3,n)
input_tasks(n,T,task_location,task_skills,budget)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_skill_greedy.append(len(Asg))
sat_skill_greedy.append(s)
time_skill_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('--------------------------------------------------')
assignments_skill_gt.append(len(Asg))
sat_skill_gt.append(s)
time_skill_gt.append(end-start)

# no of task skills = 4
print('---------------------No of task skills = 4---------------------')
T=[]
input_skills(4,n)
input_tasks(n,T,task_location,task_skills,budget)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_skill_greedy.append(len(Asg))
sat_skill_greedy.append(s)
time_skill_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('--------------------------------------------------')
assignments_skill_gt.append(len(Asg))
sat_skill_gt.append(s)
time_skill_gt.append(end-start)

# no of task skills = 5
print('---------------------No of task skills = 5---------------------')
T=[]
input_skills(5,n)
input_tasks(n,T,task_location,task_skills,budget)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_skill_greedy.append(len(Asg))
sat_skill_greedy.append(s)
time_skill_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('--------------------------------------------------')
assignments_skill_gt.append(len(Asg))
sat_skill_gt.append(s)
time_skill_gt.append(end-start)

# no of task skills = 6
print('---------------------No of task skills = 6---------------------')
T=[]
input_skills(6,n)
input_tasks(n,T,task_location,task_skills,budget)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by CAG Algorithm:',end-start,'seconds')
assignments_skill_greedy.append(len(Asg))
sat_skill_greedy.append(s)
time_skill_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('Time taken by GT algorithm:',end-start,'seconds')
print('--------------------------------------------------')
assignments_skill_gt.append(len(Asg))
sat_skill_gt.append(s)
time_skill_gt.append(end-start)

plt.plot([3,4,5,6],assignments_skill_greedy,label='CAG Algorithm')
plt.plot([3,4,5,6],assignments_skill_gt,label='GT Algorithm')
plt.xlabel('No of task skills')
plt.ylabel('No of assignments')
plt.title('No of assignments vs No of task skills')
plt.legend()
plt.show()

plt.plot([3,4,5,6],sat_skill_greedy,label='CAG Algorithm')
plt.plot([3,4,5,6],sat_skill_gt,label='GT Algorithm')
plt.xlabel('No of task skills')
plt.ylabel('Satisfaction score')
plt.title('Satisfaction score vs No of task skills')
plt.legend()
plt.show()

plt.plot([3,4,5,6],time_skill_greedy,label='CAG Algorithm')
plt.plot([3,4,5,6],time_skill_gt,label='GT Algorithm')
plt.xlabel('No of task skills')
plt.ylabel('Time taken')
plt.title('Time taken vs No of task skills')
plt.legend()
plt.show()