import random

num_workers = 500
min_longitude = 8.4
max_longitude = 37.6
min_latitude = 68.7
max_latitude = 97.4

for worker_id in range(1, num_workers + 1):
    longitude = round(random.uniform(min_longitude, max_longitude), 4)
    latitude = round(random.uniform(min_latitude, max_latitude), 4)
    print(f"{worker_id},{longitude},{latitude}")
