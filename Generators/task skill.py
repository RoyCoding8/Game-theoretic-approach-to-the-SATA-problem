import random

num_tasks = 500
max_skills_per_task = 5
num_skills = 10

for task in range(1, num_tasks + 1):
    num_skills_required = random.randint(1, max_skills_per_task)
    skills_required = random.sample(range(1, num_skills + 1), num_skills_required)
    for skill in skills_required:
        print(f"{task},{skill}")