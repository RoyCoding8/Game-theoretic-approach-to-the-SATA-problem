import sys
import os
sys.path.append(os.getcwd())

from data.generators.start import *
from src.probabilistic.monte_carlo import *

T = []
input_tasks(n,T,task_location,task_skills,budget)

asg_greedy,asg_gt=0,0
sat_score_greedy,sat_score_gt=0,0
assignments_greedy, assignments_gt = [],[]
sat_greedy, sat_gt = [],[]
time = []

start = tm.time()
NUM_SAMPLES = 500

for _ in range(NUM_SAMPLES):
    # Sample skills for uncertain workers
    # ws_incmp comes from Gen_input (via Start)
    sampled = sample_skills(ws_incmp)
    
    # Update worker skills for this simulation
    # worker_skills is the global list from Gen_input. 
    # We need to be careful not to permanently mutate it if it's reused, 
    # but here we overwrite it every time for the uncertain workers.
    # Note: Gen_input loads 'worker_skills' from csv. 
    # The loop in original main.py was: worker_skills[j+1] = all_subsets[i][j]
    # Here we do:
    for worker_idx, skills in sampled.items():
        worker_skills[worker_idx] = skills

    W = []
    # Re-create workers with the specific skills for this simulation
    input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)
    
    # Run Greedy
    Asg = greedy(T,W)[0]
    s = Cal_Sat(Asg)
    asg_greedy += len(Asg)
    sat_score_greedy += s

    # Run GT
    Asg = GT_algo(T,W)
    s = Cal_Sat(Asg)
    asg_gt += len(Asg)
    sat_score_gt += s

# Average results
asg_greedy /= NUM_SAMPLES
sat_score_greedy /= NUM_SAMPLES
asg_gt /= NUM_SAMPLES
sat_score_gt /= NUM_SAMPLES

end = tm.time()

assignments_greedy.append(asg_greedy)
sat_greedy.append(sat_score_greedy)

assignments_gt.append(asg_gt)
sat_gt.append(sat_score_gt)
time.append(end-start)

print("Experiment Results (Monte Carlo, 500 samples):")
print(f"Greedy - Avg Assignments: {asg_greedy:.2f}, Avg Satisfaction: {sat_score_greedy:.2f}")
print(f"GT     - Avg Assignments: {asg_gt:.2f},     Avg Satisfaction: {sat_score_gt:.2f}")
print(f"Time Taken: {end-start:.2f}s")

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