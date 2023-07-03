from Start import *
import matplotlib.pyplot as plt
import time as tm

# ---------------------------------------- Effect of budget ----------------------------------

from Gen_input import *

asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
assignments_greedy, assignments_gt = [],[]
sat_greedy, sat_gt = [],[]
time = []

# task budget = 200000
budget = [200000 for _ in range(n+1)]
start = tm.time()
T = []
input_tasks(n,T,task_location,task_skills,budget)
for i in range(len(all_subsets)):
    probability = all_prob[i]
    for j in range(len(all_subsets[i])):
        worker_skills[j+1] = all_subsets[i][j]
    W = []
    input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
    Asg = greedy(T,W)[0]
    s = Cal_Sat(Asg)
    asg_greedy+=len(Asg)*probability
    sat_score_greedy+=s*probability

    Asg = GT_algo(T,W)
    s = Cal_Sat(Asg)
    asg_gt+=len(Asg)*probability
    sat_score_gt+=s*probability
end = tm.time()

assignments_greedy.append(asg_greedy)
sat_greedy.append(sat_score_greedy)

assignments_gt.append(asg_gt)
sat_gt.append(sat_score_gt)
time.append(end-start)

# task budget = 300000
asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
budget = [300000 for _ in range(n+1)]
start = tm.time()
T = []
input_tasks(n,T,task_location,task_skills,budget)
for i in range(len(all_subsets)):
    probability = all_prob[i]
    for j in range(len(all_subsets[i])):
        worker_skills[j+1] = all_subsets[i][j]
    W = []
    input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
    Asg = greedy(T,W)[0]
    s = Cal_Sat(Asg)
    asg_greedy+=len(Asg)*probability
    sat_score_greedy+=s*probability

    Asg = GT_algo(T,W)
    s = Cal_Sat(Asg)
    asg_gt+=len(Asg)*probability
    sat_score_gt+=s*probability
end = tm.time()

assignments_greedy.append(asg_greedy)
sat_greedy.append(sat_score_greedy)

assignments_gt.append(asg_gt)
sat_gt.append(sat_score_gt)
time.append(end-start)

# task budget = 400000
asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
budget = [400000 for _ in range(n+1)]
start = tm.time()
T = []
input_tasks(n,T,task_location,task_skills,budget)
for i in range(len(all_subsets)):
    probability = all_prob[i]
    for j in range(len(all_subsets[i])):
        worker_skills[j+1] = all_subsets[i][j]
    W = []
    input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
    Asg = greedy(T,W)[0]
    s = Cal_Sat(Asg)
    asg_greedy+=len(Asg)*probability
    sat_score_greedy+=s*probability

    Asg = GT_algo(T,W)
    s = Cal_Sat(Asg)
    asg_gt+=len(Asg)*probability
    sat_score_gt+=s*probability
end = tm.time()

assignments_greedy.append(asg_greedy)
sat_greedy.append(sat_score_greedy)

assignments_gt.append(asg_gt)
sat_gt.append(sat_score_gt)
time.append(end-start)

# task budget = 500000
asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
budget = [500000 for _ in range(n+1)]
start = tm.time()
T = []
input_tasks(n,T,task_location,task_skills,budget)
for i in range(len(all_subsets)):
    probability = all_prob[i]
    for j in range(len(all_subsets[i])):
        worker_skills[j+1] = all_subsets[i][j]
    W = []
    input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
    Asg = greedy(T,W)[0]
    s = Cal_Sat(Asg)
    asg_greedy+=len(Asg)*probability
    sat_score_greedy+=s*probability

    Asg = GT_algo(T,W)
    s = Cal_Sat(Asg)
    asg_gt+=len(Asg)*probability
    sat_score_gt+=s*probability
end = tm.time()

assignments_greedy.append(asg_greedy)
sat_greedy.append(sat_score_greedy)

assignments_gt.append(asg_gt)
sat_gt.append(sat_score_gt)
time.append(end-start)

# ------------------------ Normalization of satisfaction score -----------------------------

mx = max(max(sat_greedy),max(sat_gt))
mn = 0
sat_greedy = [(i-mn)*100/(mx-mn) for i in sat_greedy]
sat_gt = [(i-mn)*100/(mx-mn) for i in sat_gt]

# --------------------------- Printing the values -----------------------------------

print('----------------- Budget = 20000 ----------------')
print('Expected no of assignments by CAG algorithm:',assignments_greedy[0])
print('Expected satisfaction score of the assignment:',sat_greedy[0])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[0])
print('Expected satisfaction score of the assignment:',sat_gt[0])
print('\nTime Taken:',time[0],'seconds')
print('------------------------------------------------')

print('----------------- Budget = 30000 ----------------')
print('Expected no of assignments by CAG algorithm:',assignments_greedy[1])
print('Expected satisfaction score of the assignment:',sat_greedy[1])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[1])
print('Expected satisfaction score of the assignment:',sat_gt[1])
print('\nTime Taken:',time[1],'seconds')
print('------------------------------------------------')

print('----------------- Budget = 40000 ----------------')
print('Expected no of assignments by CAG algorithm:',assignments_greedy[2])
print('Expected satisfaction score of the assignment:',sat_greedy[2])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[2])
print('Expected satisfaction score of the assignment:',sat_gt[2])
print('\nTime Taken:',time[2],'seconds')
print('------------------------------------------------')

print('----------------- Budget = 50000 ----------------')
print('Expected no of assignments by CAG algorithm:',assignments_greedy[3])
print('Expected satisfaction score of the assignment:',sat_greedy[3])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[3])
print('Expected satisfaction score of the assignment:',sat_gt[3])
print('\nTime Taken:',time[3],'seconds')
print('------------------------------------------------')

# --------------------------- Plotting the values -----------------------------------

plt.plot([20000,30000,40000,50000],assignments_greedy,label='CAG')
plt.plot([20000,30000,40000,50000],assignments_gt,label='GT')
plt.xlabel('Task Budget')
plt.ylabel('Expected no of assignments')
plt.legend()
plt.show()

plt.plot([20000,30000,40000,50000],sat_greedy,label='CAG')
plt.plot([20000,30000,40000,50000],sat_gt,label='GT')
plt.xlabel('Task Budget')
plt.ylabel('Expected satisfaction score')
plt.legend()
plt.show()

plt.plot([20000,30000,40000,50000],time)
plt.xlabel('Task Budget')
plt.ylabel('Time Taken')
plt.show()

# -------------------------------------------------------------------------------------------------------