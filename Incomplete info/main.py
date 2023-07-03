from Start import *

T = []
input_tasks(n,T,task_location,task_skills,budget)

asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
assignments_greedy, assignments_gt = [],[]
sat_greedy, sat_gt = [],[]
time = []

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

# -------------------------------------------- Evaluation metrics --------------------------------------------

# main.py (this) file has the generated input for 100 workers and 100 tasks

# Effect_of_tasks.py file shows the behaviour of No of Assignments, Satisfaction scores and Time taken with respect to the number of tasks

# Effect_of_complete_info_worker_no.py file shows the behaviour of No of Assignments, Satisfaction scores and Time taken with respect to the number of workers with complete information

# Effect_of_incomplete_info_worker_no.py file shows the behaviour of No of Assignments, Satisfaction scores and Time taken with respect to the number of workers with incomplete information

# Effect_of_skills_of_incomplete_workers.py file shows the behaviour of No of Assignments, Satisfaction scores and Time taken with respect to the number of skills of the worker with incomplete information

# Effect_of_cost.py file shows the behaviour of No of Assignments, Satisfaction scores and Time taken with respect to the worker cost

# Effect_of_budget.py file shows the behaviour of No of Assignments, Satisfaction scores and Time taken with respect to the task budget

# Effect_of_ranges.py file shows the behaviour of No of Assignments, Satisfaction scores and Time taken with respect to the range of the workers

# Effect_of_task_skills.py file shows the behaviour of No of Assignments, Satisfaction scores and Time taken with respect to the number of task skills

# Effect_of_worker_skills.py file shows the behaviour of No of Assignments, Satisfaction scores and Time taken with respect to the number of worker skills