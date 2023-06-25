import random

num_workers = 500
max_skills_per_worker = 5
num_skills = 10

for w in range(1, num_workers + 1):
    num_skills_required = random.randint(1, max_skills_per_worker)
    skills_required = random.sample(range(1, num_skills + 1), num_skills_required)
    for skill in skills_required:
        print(f"{w},{skill}")
