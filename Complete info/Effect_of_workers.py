from Original import *
import matplotlib.pyplot as plt
import time as tm

# --------------------Now using synthetic dataset to study the effect of no of workers-----------------------

# 300 workers
T,W=[],[]
from Input_w1 import *
from Input_t0 import *
input_tasks(n,T,task_location,task_skills,budget)
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)

start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
assignments_worker_greedy.append(len(Asg))
sat_worker_greedy.append(s)
time_worker_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
assignments_worker_gt.append(len(Asg))
sat_worker_gt.append(s)
time_worker_gt.append(end-start)

# 400 workers
W=[]
from Input_w2 import *
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)

start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
assignments_worker_greedy.append(len(Asg))
sat_worker_greedy.append(s)
time_worker_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
assignments_worker_gt.append(len(Asg))
sat_worker_gt.append(s)
time_worker_gt.append(end-start)

# 500 workers
W=[]
from Input_w3 import *
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)

start=tm.time()
Asg=greedy(T,W)[0]
end=tm.time()
s = Cal_Sat(Asg)
assignments_worker_greedy.append(len(Asg))
sat_worker_greedy.append(s)
time_worker_greedy.append(end-start)

start=tm.time()
Asg=GT_algo(T,W)
end=tm.time()
s = Cal_Sat(Asg)
assignments_worker_gt.append(len(Asg))
sat_worker_gt.append(s)
time_worker_gt.append(end-start)

#  -------------------------  Normalization of satisfaction score ----------------------------------

mx = max(max(sat_worker_greedy),max(sat_worker_gt))
mn = 0
sat_worker_greedy = [(i-mn)*100/(mx-mn) for i in sat_worker_greedy]
sat_worker_gt = [(i-mn)*100/(mx-mn) for i in sat_worker_gt]

#  ---------------------------------  Printing the values --------------------------------------------

print('----------------- 100 workers ----------------')
print('No of assignments by Greedy algorithm:',assignments_task_greedy[0])
print('Satisfaction score of the assignment:',sat_task_greedy[0])
print('Time taken by the Greedy Algorithm:',time_task_greedy[0])

print('\nNo of assignments by GT algorithm:',assignments_task_gt[0])
print('Satisfaction score of the assignment:',sat_task_gt[0])
print('Time taken by the GT Algorithm:',time_task_gt[0])
print('-----------------------------------------------')

print('----------------- 300 workers ----------------')
print('No of assignments by Greedy algorithm:',assignments_worker_greedy[1])
print('Satisfaction score of the assignment:',sat_worker_greedy[1])
print('Time taken by the Greedy Algorithm:',time_worker_greedy[1])

print('\nNo of assignments by GT algorithm:',assignments_worker_gt[1])
print('Satisfaction score of the assignment:',sat_worker_gt[1])
print('Time taken by the GT Algorithm:',time_worker_gt[1])
print('-----------------------------------------------')

print('----------------- 400 workers ----------------')
print('No of assignments by Greedy algorithm:',assignments_worker_greedy[2])
print('Satisfaction score of the assignment:',sat_worker_greedy[2])
print('Time taken by the Greedy Algorithm:',time_worker_greedy[2])

print('\nNo of assignments by GT algorithm:',assignments_worker_gt[2])
print('Satisfaction score of the assignment:',sat_worker_gt[2])
print('Time taken by the GT Algorithm:',time_worker_gt[2])
print('-----------------------------------------------')

print('----------------- 500 workers ----------------')
print('No of assignments by Greedy algorithm:',assignments_worker_greedy[3])
print('Satisfaction score of the assignment:',sat_worker_greedy[3])
print('Time taken by the Greedy Algorithm:',time_worker_greedy[3])

print('\nNo of assignments by GT algorithm:',assignments_worker_gt[3])
print('Satisfaction score of the assignment:',sat_worker_gt[3])
print('Time taken by the GT Algorithm:',time_worker_gt[3])
print('-----------------------------------------------')

#  ----------------------------------------  Plotting the values -------------------------------------------  

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