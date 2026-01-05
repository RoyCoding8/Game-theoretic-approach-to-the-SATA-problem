from .greedy import *
from src.common.utils import *

def GT_algo(T:list[task],W:list[worker]) -> set[tuple[worker,task]]:
    
    # get initial assignment and unassigned workers
    # Asg is a set of (worker, task)
    # u is a set of unassigned workers
    Asg, u = greedy(T,W)
    
    # Current Mapping
    worker_to_task = dict[worker, task]()
    task_to_workers = dict[int, list[worker]]()

    # Initialize mappings
    for t in T:
        task_to_workers[t.ind] = []
        
    for w, t in Asg:
        worker_to_task[w] = t
        task_to_workers[t.ind].append(w)
        
    # Unassigned workers are not in worker_to_task

    while True:
        best_move_gain = 0
        best_worker = None
        best_target_task = None # None means move to unassigned

        all_workers = W # Iterate all workers

        for w in all_workers:
            current_task = worker_to_task.get(w) # None if unassigned
            
            # --- Calculate Loss if leaving current task ---
            loss_old = 0
            if current_task:
                # Current Sat
                curr_sat = sat(current_task, task_to_workers[current_task.ind])
                # Sat if removed
                workers_after_remove = rm_el(task_to_workers[current_task.ind], w)
                
                # If removing w makes the old task invalid (e.g. skills not covered),
                # the paper's utility definition is strictly about Satisfaction Score.
                # Usually, invalid task = 0 satisfaction or -infinity.
                # However, the paper implies we optimize SATISFACTION. 
                # If a task becomes invalid, satisfaction drops to 0? Defines valid valid pair.
                # We will assume if invalid, sat is 0.
                if check_validity(current_task, workers_after_remove):
                     new_sat_old = sat(current_task, workers_after_remove)
                else:
                     new_sat_old = 0
                
                loss_old = new_sat_old - curr_sat # This will be negative
            
            # --- Evaluate options ---
            
            # Option 1: Move to Unassigned
            if current_task is not None:
                gain = loss_old
                if gain > best_move_gain:
                    best_move_gain = gain
                    best_worker = w
                    best_target_task = None
            
            # Option 2: Move to Task t_j
            for t in T:
                if current_task and t.ind == current_task.ind:
                    continue # Stay in current task - gain 0
                
                # Check if w can technically join t (constraints check on individual level)
                if not check_worker(t, w):
                    continue
                
                # Simulate adding w to t
                target_workers = task_to_workers[t.ind]
                tentative_workers = target_workers + [w]
                
                # Check group validity (Disjoint skills, etc)
                # Note: validity implies checks for budget, disjoint skills, skill coverage(maybe?)
                # Paper: "Candidate Worker Set... satisfy constraints". 
                # If we move w to t, and the resulting set is NOT valid, we cannot do it?
                # Or is utility just low? Usually constraints are hard.
                if not check_validity(t, tentative_workers):
                    continue
                
                # Calculate Gain in new task
                # Sat before (if valid)
                sat_before = 0
                if check_validity(t, target_workers):
                    sat_before = sat(t, target_workers)
                else: 
                    # If target used to be invalid (e.g. missing skills), and adding w makes it valid
                    # sat_before is 0.
                    sat_before = 0
                
                sat_after = sat(t, tentative_workers)
                
                gain_new = sat_after - sat_before
                
                total_gain = gain_new + loss_old
                
                if total_gain > best_move_gain:
                    best_move_gain = total_gain
                    best_worker = w
                    best_target_task = t

        # Perform the best move
        if best_move_gain > 1e-9 and best_worker is not None: # Use epsilon to avoid float jitter
             w = best_worker
             old_task = worker_to_task.get(w)
             new_task = best_target_task
             
             # Remove from old
             if old_task:
                 task_to_workers[old_task.ind] = rm_el(task_to_workers[old_task.ind], w)
                 del worker_to_task[w]
                 u.add(w)
            
             # Add to new
             if new_task:
                 task_to_workers[new_task.ind].append(w)
                 worker_to_task[w] = new_task
                 if w in u:
                     u.remove(w)
        else:
            break # Nash Equilibrium Reached

    Asg.clear() 
    for w, t in worker_to_task.items():
        Asg.add((w, t))

    return Asg