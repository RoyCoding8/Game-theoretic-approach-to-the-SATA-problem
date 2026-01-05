from .utils import *

def Cal_Sat(Asg:set[tuple[worker,task]]):

    # Intitialize the satisfaction of the assignment
    sum=0

    # Create a hashmap of task id and the worker set assigned to it
    tw=dict[task,list[worker]]()

    for i in Asg:
        if i[1] not in tw:
            tw[i[1]]=list[worker]()
        tw[i[1]].append(i[0])

    # Calculate the satisfaction of each task-worker set and add it to the sum
    for it in tw:
        sum+=sat(it,tw[it])

    return sum