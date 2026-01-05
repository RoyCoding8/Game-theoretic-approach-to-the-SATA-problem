import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import matplotlib.pyplot as plt
import time as tm
from src.algorithms.greedy import greedy
from src.algorithms.gt import GT_algo
from src.common.utils import sat
from data.generators.gen_input import n, budget, task_location, task_skills, worker_location, worker_range, worker_cost, worker_skills, task_history
from data.generators.start import input_tasks, input_workers

def cal_sat(Asg):
    return sum(sat(t, [w]) for w, t in Asg)

def run(worker_counts):
    results = {'workers': worker_counts, 'cag_asg': [], 'cag_sat': [], 'cag_time': [], 'gt_asg': [], 'gt_sat': [], 'gt_time': []}
    
    for m_count in worker_counts:
        print(f"Workers = {m_count}...")
        T = []
        input_tasks(n, T, task_location, task_skills, budget)
        W = []
        input_workers(min(m_count, len(worker_location)-1), W, worker_location, worker_range, worker_cost, worker_skills, task_history)
        
        t0 = tm.time()
        asg, _ = greedy(T, W)
        results['cag_asg'].append(len(asg))
        results['cag_sat'].append(cal_sat(asg))
        results['cag_time'].append(tm.time() - t0)
        
        t0 = tm.time()
        asg = GT_algo(T, W)
        results['gt_asg'].append(len(asg))
        results['gt_sat'].append(cal_sat(asg))
        results['gt_time'].append(tm.time() - t0)
    
    return results

def plot(results):
    x = results['workers']
    
    plt.figure()
    plt.plot(x, results['cag_asg'], 'b-o', label='CAG')
    plt.plot(x, results['gt_asg'], 'r-s', label='GT')
    plt.xlabel('Workers'); plt.ylabel('Assignments'); plt.legend(); plt.grid(alpha=0.3)
    plt.savefig('experiments/deterministic/workers_assignments.png')
    plt.show()
    
    plt.figure()
    plt.plot(x, results['cag_sat'], 'b-o', label='CAG')
    plt.plot(x, results['gt_sat'], 'r-s', label='GT')
    plt.xlabel('Workers'); plt.ylabel('Satisfaction'); plt.legend(); plt.grid(alpha=0.3)
    plt.savefig('experiments/deterministic/workers_satisfaction.png')
    plt.show()
    
    plt.figure()
    plt.plot(x, results['cag_time'], 'b-o', label='CAG')
    plt.plot(x, results['gt_time'], 'r-s', label='GT')
    plt.xlabel('Workers'); plt.ylabel('Time (s)'); plt.legend(); plt.grid(alpha=0.3)
    plt.savefig('experiments/deterministic/workers_time.png')
    plt.show()

if __name__ == "__main__":
    counts = [25, 50, 75, 100]
    results = run(counts)
    for i, c in enumerate(counts):
        print(f"W={c}: CAG({results['cag_asg'][i]}, {results['cag_sat'][i]:.2f}) GT({results['gt_asg'][i]}, {results['gt_sat'][i]:.2f})")
    plot(results)
