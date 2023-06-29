from main import *
import matplotlib.pyplot as plt

#  ------------------------  Effect of no of workers with complete information  ------------------------  #

# 150 workers, 3 have incomplete information
asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
from Input_w1 import *
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

# 200 workers, 3 have incomplete information
asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
from Input_w2 import *
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

# 250 workers, 3 have incomplete information
asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
from Input_w3 import *
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

#  -------------------------  Normalization of satisfaction score ----------------------------

mx = max(max(sat_greedy),max(sat_gt))
mn = 0
sat_greedy = [(i-mn)*100/(mx-mn) for i in sat_greedy]
sat_gt = [(i-mn)*100/(mx-mn) for i in sat_gt]

#  -------------------------------------  Printing --------------------------------------------

print('----------------- 100 workers ----------------')
print('Expected no of assignments by Greedy algorithm:',assignments_greedy[0])
print('Expected satisfaction score of the assignment:',sat_greedy[0])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[0])
print('Expected satisfaction score of the assignment:',sat_gt[0])
print('\nTime taken:',time[0])
print('-----------------------------------------------')

print('----------------- 150 workers ----------------')
print('Expected no of assignments by Greedy algorithm:',assignments_greedy[1])
print('Expected satisfaction score of the assignment:',sat_greedy[1])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[1])
print('Expected satisfaction score of the assignment:',sat_gt[1])
print('\nTime taken:',time[1])
print('-----------------------------------------------')

print('----------------- 200 workers ----------------')
print('Expected no of assignments by Greedy algorithm:',assignments_greedy[2])
print('Expected satisfaction score of the assignment:',sat_greedy[2])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[2])
print('Expected satisfaction score of the assignment:',sat_gt[2])
print('\nTime taken:',time[2])
print('-----------------------------------------------')

print('----------------- 250 workers ----------------')
print('Expected no of assignments by Greedy algorithm:',assignments_greedy[3])
print('Expected satisfaction score of the assignment:',sat_greedy[3])

print('\nExpected no of assignments by GT algorithm:',assignments_gt[3])
print('Expected satisfaction score of the assignment:',sat_gt[3])
print('\nTime taken:',time[3])
print('-----------------------------------------------')

#  ---------------------------------------------  Plotting  -------------------------------------------  

plt.plot([100,150,200,250],assignments_greedy,label='Greedy')
plt.plot([100,150,200,250],assignments_gt,label='GT')
plt.xlabel('No of workers')
plt.ylabel('Expected no of assignments')
plt.legend()
plt.show()

plt.plot([100,150,200,250],sat_greedy,label='Greedy')
plt.plot([100,150,200,250],sat_gt,label='GT')
plt.xlabel('No of workers')
plt.ylabel('Expected satisfaction score')
plt.legend()
plt.show()

plt.plot([100,150,200,250],time)
plt.xlabel('No of workers')
plt.ylabel('Time taken')
plt.show()