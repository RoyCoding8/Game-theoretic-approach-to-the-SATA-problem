from classes import *
import random as rd

# generate random input for input_tasks and input_workers functions
def input_tasks(i:int):
    # take location, budget and exp time as input
    l=rd.uniform(-50,50)
    b=rd.uniform(5,30)
    d=rd.randint(80,100)

    # take skill set as input
    S=[]
    for i in range(5):
        S.append(rd.randint(1,100))
    obj=task(i,l,S,b,d)
    return obj

def input_workers(i:int):
    # take location, range and travelling cost as input
    l=rd.uniform(-50,50)
    r=rd.uniform(0,3)
    v=rd.uniform(10,20)

    # take skill set as input
    S=[]
    for i in range(5):
        S.append(rd.randint(1,100))

    # take task_set as input
    T=[]
    for i in range(5):
        T.append(rd.randint(1,5))
    obj=worker(i,l,r,v,S,T)
    return obj