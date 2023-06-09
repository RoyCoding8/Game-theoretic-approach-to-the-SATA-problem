class worker:
    loc=0
    r=0
    K=[]
    task_set=[]
    cost=0
    def __init__(self,l:float,r:float,v:float,S:list,T:list) -> None:
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
    def __init__(self,l:float,S:list,b:float,d) -> None: 
        self.loc=l
        self.K_req=S
        self.budget=b
        self.expiry=d

POS_INF = float('inf')
NEG_INF = float('-inf')