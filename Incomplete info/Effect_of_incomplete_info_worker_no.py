from main import *
import matplotlib.pyplot as plt

#  ------------------------  Effect of no of workers with complete information  ------------------------  #

T = []
input_tasks(n,T,task_location,task_skills,budget)
assignments_greedy, assignments_gt = [],[]
sat_greedy, sat_gt = [],[]
time = []

# 100 workers, 1 has incomplete information
asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
from Input_iw1 import *
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

# 100 workers, 2 have incomplete information
asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
from Input_iw2 import *
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

# 100 workers, 3 have incomplete information
asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
from Input_iw3 import *
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

# --------------------------- Normalization of satisfaction score -----------------------------------

mx = max(max(sat_greedy),max(sat_gt))
mn = 0
sat_greedy = [(i-mn)*100/(mx-mn) for i in sat_greedy]
sat_gt = [(i-mn)*100/(mx-mn) for i in sat_gt]

# ------------------------------------- Printing the values -----------------------------------------

print('----------------- 1 worker with incomplete info ----------------')
print('Expected no of assignments by CAG algorithm:',assignments_greedy[0])
print('Expected satisfaction score of the assignment:',sat_greedy[0])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[0])
print('Expected satisfaction score of the assignment:',sat_gt[0])
print('\nTime Taken:',time[0],'seconds')
print('----------------------------------------------------------------')

print('----------------- 2 workers with incomplete info ----------------')
print('Expected no of assignments by CAG algorithm:',assignments_greedy[1])
print('Expected satisfaction score of the assignment:',sat_greedy[1])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[1])
print('Expected satisfaction score of the assignment:',sat_gt[1])
print('\nTime Taken:',time[1],'seconds')
print('----------------------------------------------------------------')

print('----------------- 3 workers with incomplete info ----------------')
print('Expected no of assignments by CAG algorithm:',assignments_greedy[2])
print('Expected satisfaction score of the assignment:',sat_greedy[2])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[2])
print('Expected satisfaction score of the assignment:',sat_gt[2])
print('\nTime Taken:',time[2],'seconds')
print('----------------------------------------------------------------')

# ----------------------------------------- Plotting ------------------------------------------------

plt.plot([1,2,3],assignments_greedy,label='CAG')
plt.plot([1,2,3],assignments_gt,label='GT')
plt.xlabel('No of workers with incomplete information')
plt.ylabel('Expected no of assignments')
plt.legend()
plt.show()

plt.plot([1,2,3],sat_greedy,label='CAG')
plt.plot([1,2,3],sat_gt,label='GT')
plt.xlabel('No of workers with incomplete information')
plt.ylabel('Expected satisfaction score')
plt.legend()
plt.show()

plt.plot([1,2,3],time)
plt.xlabel('No of workers with incomplete information')
plt.ylabel('Time taken')
plt.show()

# ----------------------------------------------------------------------------------------------------------