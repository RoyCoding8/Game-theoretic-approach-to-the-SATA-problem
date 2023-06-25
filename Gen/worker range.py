import random

# Generating worker-to-range mappings
worker_range_mappings = [(worker_id, round(random.uniform(8000,10000),3)) for worker_id in range(1, 501)]

# Creating a text file to store the mappings
with open("worker_range_mappings.txt", "w") as file:
    # Writing the worker-to-range mappings to the file
    for worker_id, work_range in worker_range_mappings:
        file.write(f"{worker_id},{work_range}\n")

# Confirmation message
print("Worker-to-range mappings have been written to 'worker_range_mappings.txt'.")