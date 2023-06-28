from main import *
import matplotlib.pyplot as plt

#  -----------------------------------  Effect of no of tasks  --------------------------------------  

# 150 tasks
from Input_t1 import *
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

print('----------------- 150 tasks ----------------')
print('Expected no of assignments by CAG algorithm:',asg_greedy)
print('Expected satisfaction score of the assignment:',sat_score_greedy)
assignments_greedy.append(asg_greedy)
sat_greedy.append(sat_score_greedy)

print('\nExpected no of assignments by GT algorithm:',asg_gt)
print('Expected satisfaction score of the assignment:',sat_score_gt)
print('\nTime Taken:',end-start,'seconds')
print('----------------------------------------------')
assignments_gt.append(asg_gt)
sat_gt.append(sat_score_gt)
time.append(end-start)

# 200 tasks
from Input_t2 import *
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

print('----------------- 200 tasks ----------------')
print('Expected no of assignments by CAG algorithm:',asg_greedy)
print('Expected satisfaction score of the assignment:',sat_score_greedy)
assignments_greedy.append(asg_greedy)
sat_greedy.append(sat_score_greedy)

print('\nExpected no of assignments by GT algorithm:',asg_gt)
print('Expected satisfaction score of the assignment:',sat_score_gt)
print('\nTime Taken:',end-start,'seconds')
print('----------------------------------------------')
assignments_gt.append(asg_gt)
sat_gt.append(sat_score_gt)
time.append(end-start)

# 250 tasks
from Input_t3 import *
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

print('----------------- 250 tasks ----------------')
print('Expected no of assignments by CAG algorithm:',asg_greedy)
print('Expected satisfaction score of the assignment:',sat_score_greedy)
assignments_greedy.append(asg_greedy)
sat_greedy.append(sat_score_greedy)

print('\nExpected no of assignments by GT algorithm:',asg_gt)
print('Expected satisfaction score of the assignment:',sat_score_gt)
print('\nTime Taken:',end-start,'seconds')
print('----------------------------------------------')
assignments_gt.append(asg_gt)
sat_gt.append(sat_score_gt)
time.append(end-start)

plt.plot([100,150,200,250],assignments_greedy,label='CAG')
plt.plot([100,150,200,250],assignments_gt,label='GT')
plt.xlabel('No of tasks')
plt.ylabel('Expected no of assignments')
plt.legend()
plt.show()

plt.plot([100,150,200,250],sat_greedy,label='CAG')
plt.plot([100,150,200,250],sat_gt,label='GT')
plt.xlabel('No of tasks')
plt.ylabel('Expected satisfaction score')
plt.legend()
plt.show()

# ----------------------------------------------------------------------------------------------------