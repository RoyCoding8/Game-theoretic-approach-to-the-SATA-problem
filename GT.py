from Greedy import *
from collections import deque

def GT_algo(T:list[task],W:list[worker]) -> list[tuple[worker,task]]:
    
    # get initial assignment and unassigned workers
    Asg,u=greedy(T,W)
    
    tw=dict[task,list[worker]]()
    asg=dict[worker,task]()

    # initialize the strategies
    for i in Asg:
        asg[i[0]]=i[1]
        tw[i[1]].append(i[0])

    while True:
        flg=True
        to_swap=[]
        for uw in u:
            mx=0
            flg1=False
            x=worker(0,0,0,[],[])
            for w in asg:
                if check_worker(asg[w],uw) and (uw not in to_swap):

                    # Compute difference in cooperation satisfaction on replacement
                    if len(tw[asg[w]])>1:
                        dcsat=(cop_sum(tw[asg[w]],uw)-cop_sum(tw[asg[w]],uw)-csore(uw,w))/(len(tw[asg[w]])-1)
                    else:
                        dcsat=0

                    # Compute difference price satisfaction on replacement
                    dpsat=dif_psat(asg[w],uw)-dif_psat(asg[w],w)

                    # utility computation
                    ut=dif_sat(dpsat,dcsat)     
                    if ut>mx:
                        flg=False
                        flg1=True
                        mx=ut
                        x=w
            if flg1:
                to_swap.append((uw,x))
        
        for it in to_swap:

            # it[0] is currently unassigned worker and it[1] is currently assigned worker
            asg[it[0]]=asg[it[1]]
            asg.pop(it[1])
            u.remove(it[0])
            u.add(it[1])
            
        if flg:
            break 
    
    Asg.clear()
    for key in asg:
        Asg.append((key,asg[key]))

    return Asg