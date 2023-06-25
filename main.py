# Run and print the assignment based on the Gen_input.py file

from Start import *

T,W=[],[]

# Create the task set using the input
input_tasks(n,T,task_location,task_skills,budget)

# Create the worker set using the input
input_workers(m,W,worker_location,worker_range,worker_cost,worker_skills,task_history)

# Running the program
print('--------------------------------------------------')
print('CAG algorithm assignment:\n')
Asg=greedy(T,W)[0]

# Print the assignment
Output(Asg)
print('--------------------------------------------------')

print('GT algorithm assignment:\n')
Asg=GT_algo(T,W)

# Print the assignment
Output(Asg)
print('--------------------------------------------------')

# --------------------------------- Evaluation metrics -------------------------------------

# Original.py file has the generated input for 100 workers and 100 tasks.

# Effect_of_tasks.py file shows the behaviour of No of Assignments, Satisfaction scores and Time taken with respect to the number of tasks.

# Effect_of_workers.py file shows the behaviour of No of Assignments, Satisfaction scores and Time taken with respect to the number of workers

# Effect_of_cost.py file shows the behaviour of No of Assignments, Satisfaction scores and Time taken with respect to the worker cost.

# Effect_of_budget.py file shows the behaviour of No of Assignments, Satisfaction scores and Time taken with respect to the task budget

# Effect_of_ranges.py file shows the behaviour of No of Assignments, Satisfaction scores and Time taken with respect to the range of the workers