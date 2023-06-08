from Greedy import *

"""
1) Get the greedy
2) Initialize the strategies of workers -> task they are assigned to
3) Keep track of unassigned workers and tasks those workers can complete
4) If a chosen unassigned worker also has the skills as (some worker set):

    For every worker in that set:
    a) replace the worker with the unassigned worker
    b) Check if U>0 or not, if yes the unassigned worker gets assigned to the highest U
    c) If a replacement has been done, repeat... else break

"""

def GT_algo(T:list,W:list):
    A,unassigned=greedy(T,W)
