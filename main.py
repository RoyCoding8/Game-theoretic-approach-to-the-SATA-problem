from GT import *
from Input import *

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
