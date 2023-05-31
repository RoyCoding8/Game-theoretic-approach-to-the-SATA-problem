class worker:
    loc=0
    r=0
    K=[]
    task_set=[]
    cost=0
    def __init__(self,l,r,v,S,T) -> None:
        self.loc=l
        self.r=r
        self.cost=v
        self.K=S
        self.task_set=T

class task:
    loc=0
    K_req=[]
    expiry=0
    budget=0
    def __init__(self,l,S,b,d) -> None: 
        self.loc=l
        self.K_req=S
        self.budget=b
        self.expiry=d

def input_tasks():
    # take location, budget and exp time as input
    l,b,d=map(float,input().split())

    # take skill set as input
    S=list(map(int,input().split()))
    obj=task(l,S,b,d)
    return obj

def input_workers():    
    # take location, range and travelling cost as input
    l,r,v=map(float,input().split())

    # take skill set as input
    S=list(map(int,input().split()))

    # take task_set as input
    T=list(map(int,input().split()))
    obj=worker(l,r,v,S,T)
    return obj

def csore(u:worker,v:worker):
    b,w = 0.5,0.01
    list1, list2 = u.task_set,v.task_set
    s=set()
    for i in list1:
        s.add(i)
    for i in list2:
        s.add(i)
    itr=len(s)                       # intersection
    unon=len(list1)+len(list2)-itr   # union 
    return b*w+(1-b)*itr/unon

def csat(W:list):
    n,sum = len(W),0
    if(n==1):
        return 0
    for i in range(n):
        for j in range(i):
            sum+=csore(W[i],W[j])
    return sum/(n-1)

def psat(t:task,W:list):
    sum=0
    for w in W:
        dist=abs(w.loc-t.loc)
        sum+=dist*(w.cost)
    return t.budget-sum

def sat(t:task,W:list):
    a = 0.5
    p_max,c_max=1,1     # To be decided later
    return a*psat(t,W)/p_max+(1-a)*csat(W)/c_max


l,r=map(int,input().split())

for p in range(l,r+1):
    T,W=[],[]
    
    # Input
    n = int(input()) # no of tasks
    for i in range(n):
        T.append(input_tasks())
    m = int(input()) # no of workers
    for i in range(n):
        W.append(input_workers())
    