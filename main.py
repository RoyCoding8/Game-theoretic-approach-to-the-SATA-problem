class worker:
    loc=0
    range=0
    K=[]
    task_set=[]
    cost=0
    def __init__(self,l,r,v,S,T) -> None:
        self.loc=l
        self.range=r
        self.cost=v
        self.K=S
        self.task_set=T

class task:
    loc=0
    K_req=[]
    exp=0
    budget=0
    def __init__(self,l,S,b,d) -> None: 
        self.loc=l
        self.K_req=S
        self.budget=b
        self.exp=d

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

l,r=map(int,input().split())

for p in range(l,r+1):
    T,W=[],[]
    # input tasks
    n = int(input()) # no of tasks
    for i in range(n):
        T.append(input_tasks())
    m = int(input()) # no of workers
    for i in range(n):
        W.append(input_workers())