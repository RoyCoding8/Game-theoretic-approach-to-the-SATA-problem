import random

num_tasks = 100
max_skills_per_task = random.randint(1, 6)
num_skills = 6

for task in range(1, num_tasks + 1):
    num_skills_required = random.randint(1, max_skills_per_task)
    skills_required = random.sample(range(1, num_skills + 1), num_skills_required)
    for skill in skills_required:
        print(f"{task},{skill}")