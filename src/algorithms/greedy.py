from src.common.utils import *

"""
1) Create CWS for each task

2) For every task, find the worker set with highest satisfaction

3) In case of conflict workers, keep the worker in the worker set leading to highest satisfaction increment

4) The workers not yet assigned are assigned to remaining tasks as singleton CWS with highest possible sat increment. If it is not possible to assign the worker in any task, keep the worker unassigned. 

5) Return the assignment and unassigned workers

"""

def greedy(T:list[task],W:list[worker]) -> tuple[set[tuple[worker,task]],set[worker]]:
    # The set of final assignments
    Asg=set[tuple[worker,task]]()

    # A hashmap storing the worker set for each task id
    tw=dict[int,list[worker]]()

    # A hashmap storing task id as key and determining whether the worker set is a conflict worker or not 
    mark=dict[int,bool]()

    # keep track of unassigned workers 
    unassigned=set()

    # Using this sets later when O(1) deletion is required
    W_set,T_set=set(W),set(T)

    for t in T:

        # Create the CWS for each task (w_set)
        w_set=list[worker]()
        for w in W:
            if(check_worker(t,w)):  # O(1)
                w_set.append(w)
        
        l=list[worker]()
        st=0
        mx=NEG_INF
        cop,cop1=0,0

        for i in w_set:
            cop+=cop_sum(l,i)
            if len(l)>0:
                cop1=cop/len(l)
            else:
                cop1=0
            tmp=dif_psat(t,i)

            # pick workers greedily (only when satisfaction increases)
            if (st+dif_sat(tmp,cop1))>mx:
                st+=dif_sat(tmp,cop1)
                mx=st
                l.append(i)
            else:
                cop-=cop_sum(l,i)
        
        # Add the CWS with the highest satisfaction to the hashmap corresponding to the task id
        tw[t.ind]=l

        # Intitialise mark
        mark[t.ind]=False 

    
    while True:
        n=len(T)
        flg=True
        Wc=list[worker]()
        for i in range(n):
            for j in range(i):

                # Check if the tasks T[i] and T[j] are not yet processed
                if T[i].ind in tw and T[j].ind in tw:

                    # Find the conflict workers between the two tasks
                    Wc=set_itr(tw[T[i].ind],tw[T[j].ind])

                    # Precomputation for the following loop
                    ci,cj=csat(tw[T[i].ind]),csat(tw[T[i].ind])

                    # If there are conflict workers
                    if Wc:

                        # Even if one conflict worker is present, the while loop will not break
                        flg=False

                        # Mark the tasks as ones having conflict workers 
                        mark[T[i].ind]=mark[T[j].ind]=True

                        for wc in Wc:

                            # Use precomputation to compute difference in csat with reduced time complexity
                            if len(tw[T[i].ind])>2:
                                cop=(ci-cop_sum(tw[T[i].ind],wc))/(len(tw[T[i].ind])-2)
                            else:
                                cop=0
                            tmp=dif_psat(T[i],wc)

                            # Compute the satisfaction increment for T[i]
                            di=-dif_sat(tmp,cop)
                            if len(tw[T[j].ind])>2:
                                cop=(cj-cop_sum(tw[T[j].ind],wc))/(len(tw[T[j].ind])-2)
                            else:
                                cop=0
                            tmp=dif_psat(T[j],wc)

                            # Compute the satisfaction increment for T[j]
                            dj=-dif_sat(tmp,cop)

                            # Remove the conflict workers from the worker set of the task with lower satisfaction increment
                            if di<dj:
                                tw[T[i].ind]=rm_el(tw[T[i].ind],wc)
                            else:
                                tw[T[j].ind]=rm_el(tw[T[j].ind],wc)
        if flg:
            break

        # Store the tasks that have been processed for conflict workers in l
        l=list[int]()
        
        for key in tw:

            # If the task has conflict workers
            if mark[key]:
                if(check_CWS(T[key-1],tw[key])):
                    # If the task can be completed by the worker, assign the task to the worker
                    if key in T_set:
                        T_set.remove(key)
                    for i in tw[key]:
                        Asg.add((i,T[key-1]))
                        W_set.remove(i)
                else:
                    # If the task cannot be completed by the worker, keep the worker unassigned
                    for i in tw[key]:
                        unassigned.add(i)
                        W_set.remove(i)
                l.append(key)

        # Remove the processed tasks from the hashmap
        for i in l:
            tw.pop(i)
            mark.pop(i)

    # If the worker and task set is not empty yet
    while W_set and T_set:
        
        # Assign singletons to the remaining tasks
        mx=NEG_INF
        cop=0
        x=task(0,0,0,[],0,0)
        y=worker(0,0,0,0,0,[],[])

        for t in T_set:
            for w in W_set:
                cop=sat(t,[w])  # O(1)
                if cop>mx:
                    mx=cop
                    x,y=t,w
        
        if(check_CWS(x,[y])):
            # If the worker can complete the task, assign the task to the worker
            T_set.remove(x)
            Asg.add((y,x))
        else:
            # Otherwise keep the worker unassigned
            unassigned.add(y)
        W_set.remove(y)

        # If W_set and T_set are still non-empty, repeat
    
    return Asg,unassigned