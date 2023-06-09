from classes import *

def set_itr(l1:list,l2:list):   # Compute intersection
    s=set()
    s1,s2=set(l1),set(l2)
    for i in l1:
        s.add(i)
    for i in l2:
        s.add(i)
    l=[]
    for i in s:
        if (i in s1) and (i in s2):
            l.append(i)
    return l

def csore(u:worker,v:worker):
    b,w = 0.5,0.01
    list1, list2 = u.task_set,v.task_set
    itr=len(set_itr(list1,list2))
    unon=len(list1)+len(list2)-itr 
    return b*w+(1-b)*itr/unon

def csat(W:list[worker]):
    n,sum = len(W),0
    for i in range(n):
        for j in range(i):
            sum+=csore(W[i],W[j])
    return sum/(n-1)

def psat(t:task,W:list[worker]):
    sum=0
    for w in W:
        dist=abs(w.loc-t.loc)
        sum+=dist*(w.cost)
    return t.budget-sum

def sat(t:task,W:list[worker]):
    a = 0.5
    p_max,c_max=1,1     # To be decided later
    return a*psat(t,W)/p_max+(1-a)*csat(W)/c_max

def check_worker(t:task,w:worker):
    if len(set_itr(t.K_req,w.K))==0:
       return False
    dist=abs(w.loc-t.loc)
    if(dist>w.r):
        return False
    return True

def check_CWS(t:task,W:list[worker]):
    for w in W:
        if check_worker(t,w)==False:
            return False
    return True

def rm_el(a,w):
    s=set(a)
    s.remove(w)
    return list(s)

def dif_psat(t:task,w:worker):
    dist=abs(w.loc-t.loc)
    return -w.cost*dist


# If c_sat is undivided, it will be just sum of all cooperation scores of all workers
# This function returns its difference on addition of a new worker
def dif_cop_sum(W:list[worker],w:worker):
    sum=0
    for i in W:
        sum+=csore(i,w)
    return sum

def dif_sat(t:task,W:list[worker],w:worker,dcsat:float):
    a=0.5
    p_max,c_max=1,1     # To be decided later
    return a*dif_psat(t,w)/p_max+(1-a)*dcsat/c_max