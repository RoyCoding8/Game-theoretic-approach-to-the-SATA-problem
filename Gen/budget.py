import random

# Generating task budget mappings for 300 tasks
task_budget_mappings = [(task_id, round(random.uniform(200000, 500000),3)) for task_id in range(1, 501)]

# Printing the task budget mappings
for task_id, budget in task_budget_mappings:
    print(f"{task_id},{budget}")
