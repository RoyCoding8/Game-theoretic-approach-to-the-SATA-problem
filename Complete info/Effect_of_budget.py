from Start import *
import matplotlib.pyplot as plt
import time as tm

# --------------------------Now using synthetic dataset to study the effect of task budget------------------------

from Input_t0 import *
from Input_w0 import *

# task budget = 200000
T,W=[],[]
task_budget = [200000 for _ in range(n+1)]
input_tasks(n,T,task_location,task_skills,budget)
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
assignments_budget_greedy,sat_budget_greedy,time_budget_greedy = [],[],[]
assignments_budget_gt,sat_budget_gt,time_budget_gt = [],[],[]

start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
assignments_budget_greedy.append(len(Asg))
sat_budget_greedy.append(s)
time_budget_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
assignments_budget_gt.append(len(Asg))
sat_budget_gt.append(s)
time_budget_gt.append(end-start)

# task budget = 300000
T=[]
task_budget = [300000 for _ in range(n+1)]
input_tasks(n,T,task_location,task_skills,budget)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
assignments_budget_greedy.append(len(Asg))
sat_budget_greedy.append(s)
time_budget_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
assignments_budget_gt.append(len(Asg))
sat_budget_gt.append(s)
time_budget_gt.append(end-start)

# task budget = 400000
T=[]
task_budget = [400000 for _ in range(n+1)]
input_tasks(n,T,task_location,task_skills,budget)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
assignments_budget_greedy.append(len(Asg))
sat_budget_greedy.append(s)
time_budget_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
assignments_budget_gt.append(len(Asg))
sat_budget_gt.append(s)
time_budget_gt.append(end-start)

# task budget = 500000
T=[]
task_budget = [500000 for _ in range(n+1)]
input_tasks(n,T,task_location,task_skills,budget)
start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
assignments_budget_greedy.append(len(Asg))
sat_budget_greedy.append(s)
time_budget_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
assignments_budget_gt.append(len(Asg))
sat_budget_gt.append(s)
time_budget_gt.append(end-start)

# -------------------------- Normalization of satisfaction score ----------------------------

mx = max(max(sat_budget_greedy),max(sat_budget_gt))
mn = 0
sat_budget_greedy = [(i-mn)*100/(mx-mn) for i in sat_budget_greedy]
sat_budget_gt = [(i-mn)*100/(mx-mn) for i in sat_budget_gt]

# ----------------------------------- Printing the results ---------------------------------------
print('---------------------Task budget = 200000---------------------')
print('No of assignments by CAG Algorithm:',assignments_budget_greedy[0])
print('Satisfaction score of the assignment:',sat_budget_greedy[0])
print('Time taken by CAG Algorithm:',time_budget_greedy[0],'seconds')

print('\nNo of assignments by GT algorithm:',assignments_budget_gt[0])
print('Satisfaction score of the assignment:',sat_budget_gt[0])
print('Time taken by GT algorithm:',time_budget_gt[0],'seconds')
print('--------------------------------------------------------------')

print('---------------------Task budget = 300000---------------------')
print('No of assignments by CAG Algorithm:',assignments_budget_greedy[1])
print('Satisfaction score of the assignment:',sat_budget_greedy[1])
print('Time taken by CAG Algorithm:',time_budget_greedy[1],'seconds')

print('\nNo of assignments by GT algorithm:',assignments_budget_gt[1])
print('Satisfaction score of the assignment:',sat_budget_gt[1])
print('Time taken by GT algorithm:',time_budget_gt[1],'seconds')
print('--------------------------------------------------------------')

print('---------------------Task budget = 400000---------------------')
print('No of assignments by CAG Algorithm:',assignments_budget_greedy[2])
print('Satisfaction score of the assignment:',sat_budget_greedy[2])
print('Time taken by CAG Algorithm:',time_budget_greedy[2],'seconds')

print('\nNo of assignments by GT algorithm:',assignments_budget_gt[2])
print('Satisfaction score of the assignment:',sat_budget_gt[2])
print('Time taken by GT algorithm:',time_budget_gt[2],'seconds')
print('--------------------------------------------------------------')

print('---------------------Task budget = 500000---------------------')
print('No of assignments by CAG Algorithm:',assignments_budget_greedy[3])
print('Satisfaction score of the assignment:',sat_budget_greedy[3])
print('Time taken by CAG Algorithm:',time_budget_greedy[3],'seconds')

print('\nNo of assignments by GT algorithm:',assignments_budget_gt[3])
print('Satisfaction score of the assignment:',sat_budget_gt[3])
print('Time taken by GT algorithm:',time_budget_gt[3],'seconds')
print('--------------------------------------------------------------')

# ----------------------------------- Plotting the graphs -----------------------------------------

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

plt.plot([200000,300000,400000,500000],time_budget_greedy,label='CAG')
plt.plot([200000,300000,400000,500000],time_budget_gt,label='GT')
plt.xlabel('Task budget')
plt.ylabel('Time taken')
plt.title('Time taken vs Task budget')
plt.legend()
plt.show()