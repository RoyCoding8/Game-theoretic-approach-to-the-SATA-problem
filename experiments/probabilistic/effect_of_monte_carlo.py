import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import matplotlib.pyplot as plt
import time as tm
from src.algorithms.greedy import greedy
from src.algorithms.gt import GT_algo
from src.common.utils import sat
from src.probabilistic.monte_carlo import sample_skills
from data.generators.gen_input import n, m, budget, task_location, task_skills, worker_location, worker_range, worker_cost, worker_skills, task_history, ws_incmp
from data.generators.start import input_tasks, input_workers

def cal_sat(Asg):
    return sum(sat(t, [w]) for w, t in Asg)

def run(num_samples_list):
    results = {'samples': num_samples_list, 'cag_asg': [], 'cag_sat': [], 'gt_asg': [], 'gt_sat': [], 'time': []}
    
    T = []
    input_tasks(n, T, task_location, task_skills, budget)
    
    for num in num_samples_list:
        print(f"MC samples = {num}...")
        cag_a, cag_s, gt_a, gt_s = 0, 0, 0, 0
        
        t0 = tm.time()
        for _ in range(num):
            sampled = sample_skills(ws_incmp)
            curr_skills = worker_skills.copy()
            for idx, skills in sampled.items():
                curr_skills[idx] = skills
            
            W = []
            input_workers(m, W, worker_location, worker_range, worker_cost, curr_skills, task_history)
            
            asg, _ = greedy(T, W)
            cag_a += len(asg)
            cag_s += cal_sat(asg)
            
            asg = GT_algo(T, W)
            gt_a += len(asg)
            gt_s += cal_sat(asg)
        
        results['cag_asg'].append(cag_a / num)
        results['cag_sat'].append(cag_s / num)
        results['gt_asg'].append(gt_a / num)
        results['gt_sat'].append(gt_s / num)
        results['time'].append(tm.time() - t0)
    
    return results

def plot(results):
    x = results['samples']
    
    plt.figure()
    plt.plot(x, results['cag_asg'], 'b-o', label='CAG')
    plt.plot(x, results['gt_asg'], 'r-s', label='GT')
    plt.xlabel('MC Samples'); plt.ylabel('Avg Assignments'); plt.legend(); plt.grid(alpha=0.3)
    plt.savefig('experiments/probabilistic/mc_assignments.png')
    plt.show()
    
    plt.figure()
    plt.plot(x, results['cag_sat'], 'b-o', label='CAG')
    plt.plot(x, results['gt_sat'], 'r-s', label='GT')
    plt.xlabel('MC Samples'); plt.ylabel('Avg Satisfaction'); plt.legend(); plt.grid(alpha=0.3)
    plt.savefig('experiments/probabilistic/mc_satisfaction.png')
    plt.show()
    
    plt.figure()
    plt.plot(x, results['time'], 'g-^')
    plt.xlabel('MC Samples'); plt.ylabel('Time (s)'); plt.grid(alpha=0.3)
    plt.savefig('experiments/probabilistic/mc_time.png')
    plt.show()

if __name__ == "__main__":
    samples = [10, 50, 100, 200]
    results = run(samples)
    for i, s in enumerate(samples):
        print(f"S={s}: CAG({results['cag_asg'][i]:.1f}, {results['cag_sat'][i]:.2f}) GT({results['gt_asg'][i]:.1f}, {results['gt_sat'][i]:.2f}) T={results['time'][i]:.1f}s")
    plot(results)
