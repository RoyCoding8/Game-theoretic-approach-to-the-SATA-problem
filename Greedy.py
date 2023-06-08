from req_functions import *

"""
1) Create CWS for each task

2) For every task, find the worker set with highest satisfaction

3) In case of conflict workers, keep the worker in the worker set leading to highest satisfaction increment

4) the workers not yet assigned are assigned to remaining tasks as singleton CWS with highest possible sat increment. If it is not possible to assign the worker in any task, keep the worker unassigned. 

5) Return the assignment and unassigned workers

"""

def greedy(T:list,W:list):
    A=[]
    tw=dict()

    # keep track of unassigned workers 
    unassigned=[]       

    # Using this sets later when O(1) deletion is required
    W1,T1=set(W),set(T)

    for t in T:
        w_set=[]
        for w in W:
            if(check_worker(t,w)):  # O(1)
                w_set.append(w)
        
        l=[]
        st=0
        mx=NEG_INF
        
        # store csat and keep adding dif_csat to it (remove divide in dif_cast). the pass that value to dif_sat  

        for i in w_set:
            # pick workers greedily (only when satisfaction increases)
            if (st+dif_sat(t,l,i,1))>mx:
                st+=dif_sat(t,l,i,1)
                mx=st
                l.append(i)
            
        tw[t]=[l,False]
    
    while True:
        n=len(T)
        flg=True
        for i in range(n):
            for j in range(i):
                Wc=set_itr(tw[T[i]][0],tw[T[j]][0])

                # compute csat for tw[T[i][0]] & tw[T[j][0]] and use dif_csat for each wc later for actual csat difference  
                if len(Wc)>0:
                    flg=False
                    tw[T[i][1]]=tw[T[j][1]]=True
                    for wc in Wc:
                        di=-dif_sat(T[i],tw[T[i][0]],wc,1)
                        dj=-dif_sat(T[j],tw[T[j][0]],wc,1)
                        if di<dj:
                            tw[T[i][0]]=rm_el(tw[T[i][0]],wc)
                        else:
                            tw[T[i][0]]=rm_el(tw[T[i][0]],wc)
        if flg:
            break
        l=[]
        
        for key in tw:
            if tw[key][1]:
                if(check_CWS(key,tw[key][0])):
                    T1.remove(key)
                    for i in tw[key][0]:
                        A.append([i,key])
                        W1.remove(i)
                else:
                    for i in tw[key][0]:
                        unassigned.append(i)
                        W1.remove(i)
                l.append(key)

        for i in l:
            tw.pop(i)

    while W1 and T1:
        mx=NEG_INF
        tmp=0
        x=task(0,[],0,0)
        y=worker(0,0,0,[],[])
        for t in T1:
            for w in W1:
                tmp=sat(t,[w])  # O(1)
                if tmp>mx:
                    mx=tmp
                    x,y=t,w
        
        if(check_CWS(x,[y])):
            T1.remove(x)
            A.append([y,x])
        else:
            unassigned.append(y)
        W1.remove(y)
        
    return A,unassigned