import random

num_tasks = 500
min_longitude = 8.4
max_longitude = 37.6
min_latitude = 68.7
max_latitude = 97.4

for task_id in range(1, num_tasks + 1):
    longitude = round(random.uniform(min_longitude, max_longitude), 4)
    latitude = round(random.uniform(min_latitude, max_latitude), 4)
    print(f"{task_id},{longitude},{latitude}")
