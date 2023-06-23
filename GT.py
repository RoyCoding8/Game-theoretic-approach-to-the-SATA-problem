from Greedy import *

def GT_algo(T:list[task],W:list[worker]) -> set[tuple[worker,task]]:
    
    # get initial assignment and unassigned workers
    Asg,u=greedy(T,W)
    
    tw=dict[int,list[worker]]()
    asg=dict[worker,task]()

    # initialize the tw dictionary
    for i in Asg:
        tw[i[1].ind]=[]
    
    # initialize the strategies of the workers and create a task-worker mapping
    for i in Asg:
        asg[i[0]]=i[1]
        tw[i[1].ind].append(i[0])

    while True:
        flg=True
        to_swap=set[tuple[worker,worker]]()
        for uw in u:

            # mx is the maximum utility. If no change is made, utility is zero.
            mx=0
            flg1=False
            x=worker(0,0,0,0,0,[],[])
            for w in asg:
                if check_worker(asg[w],uw) and (uw not in to_swap):

                    # Compute difference in cooperation satisfaction on replacement
                    if len(tw[asg[w].ind])>1:
                        dcsat=(cop_sum(tw[asg[w].ind],uw)-cop_sum(tw[asg[w].ind],w)-csore(uw,w))/(len(tw[asg[w].ind])-1)
                    else:
                        dcsat=0

                    # Compute difference price satisfaction on replacement
                    dpsat=dif_psat(asg[w],uw)-dif_psat(asg[w],w)

                    # utility computation
                    ut=dif_sat(dpsat,dcsat) 

                    # pick the worker with the highest utility (which should be greater than zero)    
                    if ut>mx:
                        # If atleast one swap is made, don't break the while loop
                        flg=False

                        # If a swap is made for that particular, set flg1 to True to add it to the to_swap set
                        flg1=True
                        mx=ut
                        x=w
            
            # If a swap has been made, add the pair to be swapped to the to_swap set
            if flg1:
                to_swap.add((uw,x))
        
        # Swap the workers in the to_swap set
        for it in to_swap:

            # it[0] is currently unassigned worker and it[1] is currently assigned worker
            asg[it[0]]=asg[it[1]]
            asg.pop(it[1])
            u.remove(it[0])
            u.add(it[1])
        
        # If no swap is made, flg is True, so break the while loop
        if flg:
            break 
    
    Asg.clear()

    # Add the final assignment to the Asg set
    for key in asg:
        Asg.add((key,asg[key]))

    return Asg