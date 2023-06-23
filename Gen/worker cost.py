import random

# Generating task budget mappings for 300 tasks
worker_cost_mappings = [(worker_id,round(random.uniform(5, 10),3)) for worker_id in range(1, 501)]

# Printing the task budget mappings
for worker, cost in worker_cost_mappings:
    print(f"{worker},{cost}")
