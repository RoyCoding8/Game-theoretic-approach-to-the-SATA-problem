import random

N_TASKS = 100
N_WORKERS = 100
N_SKILLS = 10
N_INCOMPLETE = 3

LAT = (12.9, 13.1)
LON = (77.5, 77.7)
BUDGET = (100000, 500000)
RANGE_KM = (20, 100)
COST = (0.5, 2.0)

def gen_loc():
    return round(random.uniform(*LAT), 4), round(random.uniform(*LON), 4)

def gen_skills(lo, hi):
    return random.sample(range(1, N_SKILLS+1), random.randint(lo, min(hi, N_SKILLS)))

def generate():
    tasks = []
    for i in range(1, N_TASKS+1):
        lat, lon = gen_loc()
        tasks.append({
            'id': i, 'lat': lat, 'lon': lon,
            'budget': random.randint(*BUDGET),
            'skills': gen_skills(1, 3)
        })
    
    workers = []
    for i in range(1, N_WORKERS+1):
        lat, lon = gen_loc()
        workers.append({
            'id': i, 'lat': lat, 'lon': lon,
            'range': random.randint(*RANGE_KM),
            'cost': round(random.uniform(*COST), 2),
            'skills': gen_skills(1, 4),
            'history': random.sample(range(1, N_TASKS+1), random.randint(0, 5))
        })
    
    incomplete = []
    for i in range(1, N_INCOMPLETE+1):
        skills = gen_skills(2, 4)
        probs = [round(random.uniform(0.3, 0.9), 2) for _ in skills]
        incomplete.append({'worker': i, 'data': list(zip(probs, skills))})
    
    return tasks, workers, incomplete

if __name__ == "__main__":
    tasks, workers, incomplete = generate()
    print(f"Generated {len(tasks)} tasks, {len(workers)} workers, {len(incomplete)} incomplete")
    print(f"Sample task: {tasks[0]}")
    print(f"Sample worker: {workers[0]}")
