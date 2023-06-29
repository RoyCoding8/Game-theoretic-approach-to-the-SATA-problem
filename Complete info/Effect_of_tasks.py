from Original import *
import matplotlib.pyplot as plt
import time as tm

# ------------------------Now using synthetic dataset to study the effect of no of tasks---------------------------

# 300 tasks
T,W=[],[]
from Input_t1 import *
from Input_w0 import *
input_tasks(n,T,task_location,task_skills,budget)
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)

start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
assignments_task_greedy.append(len(Asg))
sat_task_greedy.append(s)
time_task_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
assignments_task_gt.append(len(Asg))
sat_task_gt.append(s)
time_task_gt.append(end-start)

# 400 tasks
T=[]
from Input_t2 import *
from Input_w0 import *
input_tasks(n,T,task_location,task_skills,budget)

start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
assignments_task_greedy.append(len(Asg))
sat_task_greedy.append(s)
time_task_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
assignments_task_gt.append(len(Asg))
sat_task_gt.append(s)
time_task_gt.append(end-start)

# 500 tasks
T=[]
from Input_t3 import *
from Input_w0 import *
input_tasks(n,T,task_location,task_skills,budget)

start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
assignments_task_greedy.append(len(Asg))
sat_task_greedy.append(s)
time_task_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
assignments_task_gt.append(len(Asg))
sat_task_gt.append(s)
time_task_gt.append(end-start)

# ------------------------- Normalization of satisfaction score ------------------------------------

mx = max(max(sat_task_greedy),max(sat_task_gt))
mn = 0
sat_task_greedy = [(i-mn)*100/(mx-mn) for i in sat_task_greedy]
sat_task_gt = [(i-mn)*100/(mx-mn) for i in sat_task_gt]

# --------------------------------- Printing the values --------------------------------------------

print('----------------- 100 tasks ----------------')
print('No of assignments by CAG algorithm:',assignments_task_greedy[0])
print('Satisfaction score of the assignment:',sat_task_greedy[0])
print('Time Taken by CAG Algoritm:',time_task_greedy[0],'seconds')

print('\nNo of assignments by GT algorithm:',assignments_task_gt[0])
print('Satisfaction score of the assignment:',sat_task_gt[0])
print('Time Taken by GT Algoritm:',time_task_gt[0],'seconds')
print('----------------------------------------------')

print('----------------- 300 tasks ----------------')
print('No of assignments by CAG algorithm:',assignments_task_greedy[1])
print('Satisfaction score of the assignment:',sat_task_greedy[1])
print('Time Taken by CAG Algoritm:',time_task_greedy[1],'seconds')

print('\nNo of assignments by GT algorithm:',assignments_task_gt[1])
print('Satisfaction score of the assignment:',sat_task_gt[1])
print('Time Taken by GT Algoritm:',time_task_gt[1],'seconds')
print('----------------------------------------------')

print('----------------- 400 tasks ----------------')
print('No of assignments by CAG algorithm:',assignments_task_greedy[2])
print('Satisfaction score of the assignment:',sat_task_greedy[2])
print('Time Taken by CAG Algoritm:',time_task_greedy[2],'seconds')

print('\nNo of assignments by GT algorithm:',assignments_task_gt[2])
print('Satisfaction score of the assignment:',sat_task_gt[2])
print('Time Taken by GT Algoritm:',time_task_gt[2],'seconds')
print('----------------------------------------------')

print('----------------- 500 tasks ----------------')
print('No of assignments by CAG algorithm:',assignments_task_greedy[3])
print('Satisfaction score of the assignment:',sat_task_greedy[3])
print('Time Taken by CAG Algoritm:',time_task_greedy[3],'seconds')

print('\nNo of assignments by GT algorithm:',assignments_task_gt[3])
print('Satisfaction score of the assignment:',sat_task_gt[3])
print('Time Taken by GT Algoritm:',time_task_gt[3],'seconds')
print('----------------------------------------------')

# --------------------------------- Plotting the values --------------------------------------------

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

plt.plot([100,300,400,500],time_task_greedy,label='CAG')
plt.plot([100,300,400,500],time_task_gt,label='GT')
plt.xlabel('No of tasks')
plt.ylabel('Time taken')
plt.title('Time taken vs No of tasks')
plt.legend()
plt.show()