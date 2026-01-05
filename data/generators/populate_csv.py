import csv, os
from gen_data import generate

def write_csvs(tasks, workers, incomplete):
    base = os.path.join(os.path.dirname(__file__), '..', 'raw')
    
    with open(f'{base}/task_budget.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['task','budget'])
        for t in tasks: w.writerow([t['id'], t['budget']])
    
    with open(f'{base}/task_location.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['task','latitude','longitude'])
        for t in tasks: w.writerow([t['id'], t['lat'], t['lon']])
    
    with open(f'{base}/task_skills.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['task','req_skill'])
        for t in tasks:
            for s in t['skills']: w.writerow([t['id'], s])
    
    with open(f'{base}/worker_location.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['worker','latitude','longitude'])
        for wr in workers: w.writerow([wr['id'], wr['lat'], wr['lon']])
    
    with open(f'{base}/worker_range.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['worker','range'])
        for wr in workers: w.writerow([wr['id'], wr['range']])
    
    with open(f'{base}/worker_cost.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['worker','cost'])
        for wr in workers: w.writerow([wr['id'], wr['cost']])
    
    with open(f'{base}/worker_skills.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['worker','skill'])
        for wr in workers:
            for s in wr['skills']: w.writerow([wr['id'], s])
    
    with open(f'{base}/worker_task_history.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['worker','task'])
        for wr in workers:
            for t in wr['history']: w.writerow([wr['id'], t])
    
    with open(f'{base}/worker_skills_incomplete.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['worker','probability','skill'])
        for inc in incomplete:
            for prob, skill in inc['data']: w.writerow([inc['worker'], prob, skill])
    
    print(f"Written 9 CSVs to {base}")

if __name__ == "__main__":
    tasks, workers, incomplete = generate()
    write_csvs(tasks, workers, incomplete)
