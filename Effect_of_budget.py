from Start import *

# --------------------------Now using synthetic dataset to study the effect of task budget------------------------

from Input_t0 import *
from Input_w0 import *

# task budget = 200000
T,W=[],[]
task_budget = [200000]*(n+1)
input_tasks(n,T,task_location,task_skills,budget)
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
assignments_budget_greedy,sat_budget_greedy = [],[]
assignments_budget_gt,sat_budget_gt = [],[]

print('---------------------Task budget = 200000---------------------')
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_budget_greedy.append(len(Asg))
sat_budget_greedy.append(s)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_budget_gt.append(len(Asg))
sat_budget_gt.append(s)

# task budget = 300000
print('---------------------Task budget = 300000---------------------')
T=[]
task_budget = [300000]*(n+1)
input_tasks(n,T,task_location,task_skills,budget)
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_budget_greedy.append(len(Asg))
sat_budget_greedy.append(s)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_budget_gt.append(len(Asg))
sat_budget_gt.append(s)

# task budget = 400000

print('---------------------Task budget = 400000---------------------')
T=[]
task_budget = [400000]*(n+1)
input_tasks(n,T,task_location,task_skills,budget)
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_budget_greedy.append(len(Asg))
sat_budget_greedy.append(s)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_budget_gt.append(len(Asg))
sat_budget_gt.append(s)

# task budget = 500000
print('---------------------Task budget = 500000---------------------')
T=[]
task_budget = [500000]*(n+1)
input_tasks(n,T,task_location,task_skills,budget)
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_budget_greedy.append(len(Asg))
sat_budget_greedy.append(s)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_budget_gt.append(len(Asg))
sat_budget_gt.append(s)

plt.plot([200000,300000,400000,500000],assignments_budget_greedy,label='CAG')
plt.plot([200000,300000,400000,500000],assignments_budget_gt,label='GT')
plt.xlabel('Task budget')
plt.ylabel('No of assignments')
plt.title('No of assignments vs Task budget')
plt.legend()
plt.show()

plt.plot([200000,300000,400000,500000],sat_budget_greedy,label='CAG')
plt.plot([200000,300000,400000,500000],sat_budget_gt,label='GT')
plt.xlabel('Task budget')
plt.ylabel('Satisfaction score')
plt.title('Satisfaction score vs Task budget')
plt.legend()
plt.show()