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

def set_itr(l1:list,l2:list):   # Compute intersection
    s=set()
    for i in l1:
        s.add(i)
    for i in l2:
        s.add(i)
    return list(s)

def csore(u:worker,v:worker):
    b,w = 0.5,0.01
    list1, list2 = u.task_set,v.task_set
    itr=len(set_itr(list1,list2))
    unon=len(list1)+len(list2)-itr 
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

def check_worker(t:task,w:worker):
    if len(set_itr(t.K_req,w.K))==0:
       return False
    dist=abs(w.loc-t.loc)
    if(dist>w.r):
        return False
    return True

def check_CWS(t:task,W:list):
    for w in W:
        if check_worker(t,w)==False:
            return False
    return True

def rm_el(a,w):
    s=set(a)
    s.remove(w)
    return list(s)

def greedy(T:list,W:list):
    """
    tw is a hashmap with key as task and value as corresponding [CWS,boolean].
    'boolean' represents whether the CWS has had conflicting workers on not

    """
    tw=dict()
    A=list()
    for t in T:
        w_set=list()
        # Create initial CWS for each task
        for w in W:
            if check_worker(t,w):
                w_set.append(w)
        tw[t]=[w_set,False]
        
    while True:
        n = len(T)
        flg=True
        for i in range(n):
            for j in range(i):
                Wc=set_itr(tw[T[i]][0],tw[T[j]][0])
                if len(Wc)>0:
                    flg&=(False)
                    tw[T[i]][1]=tw[T[i]][1]=True
                    for wc in Wc:
                        dif1=sat(T[i],tw[T[i]][0])-sat(T[i],rm_el(tw[T[i]][0],wc))
                        dif2=sat(T[j],tw[T[j][0]])-sat(T[j],rm_el(tw[T[j]][0],wc))
                        if dif1<dif2:
                            tw[T[i]][0]=rm_el(tw[T[i]][0],wc)
                        else:
                            tw[T[j]][0]=rm_el(tw[T[j]][0],wc)
        if flg:
            break
        l=[]
        for key in tw:
            if tw[key][1]:
                if check_CWS(key,tw[key][0]):
                    T=rm_el(T,key)
                    for it in tw[key][0]:
                        A.append((it,key))
                for w in tw[key][0]:
                    W=rm_el(W,w)
                l.append(key)

        # delete the tasks in the hashmap which are completed or whose wokers are removed
        for i in l:
            tw.pop(i)
    
    while len(W)>0 and len(T)>0:
        n,m=len(T),len(W)
        x,y=0,0
        mx=-(2**63)
        for i in range(n):
            for j in range(m):
                tmp=sat(T[i],[W[j]])
                if tmp>mx:
                    mx=tmp
                    x,y=i,j
        W=rm_el(W,W[y])
        if check_CWS(T[x],[W[y]]):
            T=rm_el(T,T[x])
            A.append((T[x],W[y]))
    return A

l,r=map(int,input().split())

for p in range(l,r+1):
    T,W=[],[]
    
    # Input (can be changed later to file based input)
    n = int(input()) # no of tasks
    for i in range(n):
        T.append(input_tasks())
    m = int(input()) # no of workers
    for i in range(n):
        W.append(input_workers())
