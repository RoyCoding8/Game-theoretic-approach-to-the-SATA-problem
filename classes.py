class worker:
    ind=0
    latitude=0
    longitude=0
    r=0
    K=list()
    task_set=list()
    cost=0
    def __init__(self,i:int,lon:float,lat:float,r:float,v:float,S:list,T:list) -> None:
        self.ind=i
        self.latitude=lat
        self.longitude=lon
        self.r=r
        self.cost=v
        self.K=S
        self.task_set=T

class task:
    ind=0
    latitude=0
    longitude=0
    K_req=list()
    expiry=0
    budget=0
    def __init__(self,i:int,lon:float,lat:float,S:list,b:float,d) -> None: 
        self.ind=i
        self.latitude=lat
        self.longitude=lon
        self.K_req=S
        self.budget=b
        self.expiry=d

POS_INF = float('inf')
NEG_INF = float('-inf')