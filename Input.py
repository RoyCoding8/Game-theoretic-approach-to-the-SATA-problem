from classes import *

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