from GT import *
from Construct_set import *
from Output import *
from Calculate_Sat import *
import time as tm

def input_tasks(n,T,task_location,task_skills,budget):
    for i in range(1,n+1):

        # Create the task object and put it in task set
        obj=task(i,task_location[i][0],task_location[i][1],task_skills[i],budget[i],POS_INF)
        T.append(obj)

def input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history):
    for i in range(1,m+1):

        # Create the worker object and put it in worker set
        obj=worker(i,worker_location[i][0],worker_location[i][1],worker_range[i],worker_cost[i],worker_skills[i],task_history[i])
        W.append(obj)

T = []
input_tasks(n,T,task_location,task_skills,budget)

no_of_asg_greedy,no_of_asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
start = tm.time()
for i in range(len(all_subsets)):
    probability = all_prob[i]
    for j in range(len(all_subsets[i])):
        worker_skills[j+1] = all_subsets[i][j]
    W = []
    input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
    Asg = greedy(T,W)[0]
    s = Cal_Sat(Asg)
    no_of_asg_greedy+=len(Asg)*probability
    sat_score_greedy+=s*probability

    Asg = GT_algo(T,W)
    s = Cal_Sat(Asg)
    no_of_asg_gt+=len(Asg)*probability
    sat_score_gt+=s*probability
end = tm.time()

print('----------------------------------------------')
print('Expected no of assignments by Greedy algorithm:',no_of_asg_greedy)
print('Expected satisfaction score of the assignment:',sat_score_greedy)

print('\nExpected no of assignments by GT algorithm:',no_of_asg_gt)
print('Expected satisfaction score of the assignment:',sat_score_gt)
print('Time Taken:',end-start,'seconds')
print('----------------------------------------------')