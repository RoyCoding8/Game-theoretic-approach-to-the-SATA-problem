from req_functions import *

"""
1) Create CWS for each task

2) For every task, find the worker set with highest satisfaction

3) In case of conflict workers, keep the worker in the worker set leading to highest satisfaction increment

4) The workers not yet assigned are assigned to remaining tasks as singleton CWS with highest possible sat increment. If it is not possible to assign the worker in any task, keep the worker unassigned. 

5) Return the assignment and unassigned workers

"""

def greedy(T:list[task],W:list[worker]) -> tuple[list[tuple[worker,task]],set[worker]]:
    Asg=[]
    tw=dict()

    # keep track of unassigned workers 
    unassigned=set()   

    # Using this sets later when O(1) deletion is required
    W_set,T_set=set(W),set(T)

    for t in T:
        w_set=[]
        for w in W:
            if(check_worker(t,w)):  # O(1)
                w_set.append(w)
        
        l=[]
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
            
        tw[t.ind]=[l,False]
    
    while True:
        n=len(T)
        flg=True
        Wc=list[worker]()
        for i in range(n):
            for j in range(i):
                Wc=set_itr(tw[T[i].ind][0],tw[T[j].ind][0])
                ci,cj=csat(tw[T[i].ind][0]),csat(tw[T[i].ind][0])
                
                if len(Wc)>0:
                    flg=False
                    tw[T[i].ind][1]=tw[T[j].ind][1]=True
                    for wc in Wc:
                        if len(tw[T[i].ind][0])>2:
                            cop=(ci-cop_sum(tw[T[i].ind][0],wc))/(len(tw[T[i].ind][0])-2)
                        else:
                            cop=0
                        tmp=dif_psat(T[i],wc)
                        di=-dif_sat(tmp,cop)
                        if len(tw[T[j].ind][0])>2:
                            cop=(cj-cop_sum(tw[T[j].ind][0],wc))/(len(tw[T[j].ind][0])-2)
                        else:
                            cop=0
                        tmp=dif_psat(T[j],wc)
                        dj=-dif_sat(tmp,cop)
                        if di<dj:
                            tw[T[i].ind][0]=rm_el(tw[T[i].ind][0],wc)
                        else:
                            tw[T[i].ind][0]=rm_el(tw[T[i].ind][0],wc)
        if flg:
            break
        l=[]
        
        for key in tw:
            if tw[key][1]:
                if(check_CWS(key,tw[key][0])):
                    if key in T_set:
                        T_set.remove(key)
                    for i in tw[key][0]:
                        Asg.append((i,key))
                        W_set.remove(i)
                else:
                    for i in tw[key][0]:
                        unassigned.add(i)
                        W_set.remove(i)
                l.append(key)

        for i in l:
            tw.pop(i)

    while W_set and T_set:
        mx=NEG_INF
        cop=0
        x=task(0,0,[],0,0)
        y=worker(0,0,0,0,[],[])
        for t in T_set:
            for w in W_set:
                cop=sat(t,[w])  # O(1)
                if cop>mx:
                    mx=cop
                    x,y=t,w
        
        if(check_CWS(x,[y])):
            T_set.remove(x)
            Asg.append((y,x))
        else:
            unassigned.add(y)
        W_set.remove(y)
        
    return Asg,unassigned