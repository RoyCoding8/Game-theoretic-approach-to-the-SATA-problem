from Start import *
import matplotlib.pyplot as plt
import time as tm

# ------------------------------------ Effect worker range ----------------------------------------

from Gen_input import *

T = []
input_tasks(n,T,task_location,task_skills,budget)
assignments_greedy, assignments_gt = [],[]
sat_greedy, sat_gt = [],[]
time = []

# Worker range = 6000
asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
worker_range = [6000 for _ in range(m+1)]
start = tm.time()
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

# worker range = 7000
asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
worker_range = [7000 for _ in range(m+1)]
start = tm.time()
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

# Worker range = 8000
asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
worker_range = [8000 for _ in range(m+1)]
start = tm.time()
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

# Worker range = 9000
asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
worker_range = [9000 for _ in range(m+1)]
start = tm.time()
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

# Worker range = 10000
asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
worker_range = [10000 for _ in range(m+1)]
start = tm.time()
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

# ------------------------- Normalization of satisfaction score -----------------------------

mx = max(max(sat_greedy),max(sat_gt))
mn = 0
sat_greedy = [(i-mn)*100/(mx-mn) for i in sat_greedy]
sat_gt = [(i-mn)*100/(mx-mn) for i in sat_gt]

# ------------------------------ Printing the values ----------------------------------------

print('----------------- Worker Range = 6000 ----------------')
print('Expected no of assignments by CAG algorithm:',assignments_greedy[0])
print('Expected satisfaction score of the assignment:',sat_greedy[0])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[0])
print('Expected satisfaction score of the assignment:',sat_gt[0])
print('\nTime Taken:',time[0],'seconds')
print('------------------------------------------------')

print('----------------- Worker Range = 7000 ----------------')
print('Expected no of assignments by CAG algorithm:',assignments_greedy[1])
print('Expected satisfaction score of the assignment:',sat_greedy[1])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[1])
print('Expected satisfaction score of the assignment:',sat_gt[1])
print('\nTime Taken:',time[1],'seconds')
print('------------------------------------------------')

print('----------------- Worker Range = 8000 ----------------')
print('Expected no of assignments by CAG algorithm:',assignments_greedy[2])
print('Expected satisfaction score of the assignment:',sat_greedy[2])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[2])
print('Expected satisfaction score of the assignment:',sat_gt[2])
print('\nTime Taken:',time[2],'seconds')
print('------------------------------------------------')

print('----------------- Worker Range = 9000 ----------------')
print('Expected no of assignments by CAG algorithm:',assignments_greedy[3])
print('Expected satisfaction score of the assignment:',sat_greedy[3])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[3])
print('Expected satisfaction score of the assignment:',sat_gt[3])
print('\nTime Taken:',time[0],'seconds')
print('------------------------------------------------')

print('----------------- Worker Range = 10000 ----------------')
print('Expected no of assignments by CAG algorithm:',assignments_greedy[4])
print('Expected satisfaction score of the assignment:',sat_greedy[4])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[4])
print('Expected satisfaction score of the assignment:',sat_gt[4])
print('\nTime Taken:',time[3],'seconds')
print('------------------------------------------------')

# ------------------------------ Plotting the values ----------------------------------------

plt.plot([6000,7000,8000,9000,10000],assignments_greedy,label='CAG')
plt.plot([6000,7000,8000,9000,10000],assignments_gt,label='GT')
plt.xlabel('Worker Range')
plt.ylabel('Expected no of assignments')
plt.legend()
plt.show()

plt.plot([6000,7000,8000,9000,10000],sat_greedy,label='CAG')
plt.plot([6000,7000,8000,9000,10000],sat_gt,label='GT')
plt.xlabel('Worker Range')
plt.ylabel('Expected satisfaction score')
plt.legend()
plt.show()

plt.plot([6000,7000,8000,9000,10000],time)
plt.xlabel('Worker Range')
plt.ylabel('Time Taken')
plt.show()

# -----------------------------------------------------------------------------------------------------------