from .classes import *
from .distance import *

def set_itr(l1:list,l2:list) -> list:   # Compute intersection
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

def csore(u:worker,v:worker) -> float:
    b,w = 0.5,0.01
    list1, list2 = u.task_set,v.task_set
    itr=len(set_itr(list1,list2))
    unon=len(list1)+len(list2)-itr
    if unon == 0:
        return b*w
    return b*w+(1-b)*itr/unon

def csat(W:list[worker]) -> float:
    n,sum = len(W),0
    if(n<=1):
        return 0
    for i in range(n):
        for j in range(i):
            sum+=csore(W[i],W[j])
    return 2*sum/(n-1)

def psat(t:task,W:list[worker]) -> float:
    sum=0
    for w in W:
        dist=calculate_distance(t.latitude,t.longitude,w.latitude,w.longitude)
        sum+=dist*(w.cost)
    return t.budget-sum

def sat(t:task,W:list[worker]) -> float:
    a=0.5
    p_max,c_max=100000,10000
    return a*psat(t,W)/p_max+(1-a)*csat(W)/c_max

def check_worker(t:task,w:worker):
    if not set_itr(t.K_req,w.K):
       return False
    dist=calculate_distance(t.latitude,t.longitude,w.latitude,w.longitude)
    if dist>w.r:
        return False
    return True

def check_validity(t:task, W:list[worker]) -> bool:
    # 1. Budget Constraint
    if psat(t,W) < 0:
        return False
    
    # 2. Skill Coverage: Union(K_w) must cover K_t
    covered_skills = set()
    for w in W:
        for s in w.K:
            covered_skills.add(s)
    
    for req in t.K_req:
        if req not in covered_skills:
            return False

    # 3. Disjoint Skills (Duplicate Constraint): K_wi intersect K_wj = empty
    n = len(W)
    for i in range(n):
        for j in range(i+1, n):
            if set_itr(W[i].K, W[j].K): # If intersection is non-empty
                return False
                
    return True

def check_CWS(t:task,W:list[worker]):
    # Check individual constraints first
    for w in W:
        if not check_worker(t,w):
            return False
    # Check group constraints
    return check_validity(t, W)

def rm_el(a,w) -> list:
    l=[]
    for i in a:
        if i!=w:
            l.append(i)
    return l

def dif_psat(t:task,w:worker) -> float:
    dist=calculate_distance(t.latitude,t.longitude,w.latitude,w.longitude)
    return -w.cost*dist


# If c_sat is undivided, it will be just sum of all cooperation scores of all workers
# This function returns its difference on addition of a new worker
def cop_sum(W:list[worker],w:worker) -> float:
    sum=0
    for i in W:
        sum+=csore(i,w)
    return sum

def dif_sat(dpsat:float,dcsat:float) -> float:
    a=0.5
    p_max,c_max=100000,10000
    return a*dpsat/p_max+(1-a)*dcsat/c_max