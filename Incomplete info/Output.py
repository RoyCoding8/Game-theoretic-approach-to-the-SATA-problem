from classes import *
from Construct_set import *

def Output(Asg:set[tuple[worker,task]]):
    A=list(Asg)
    A.sort(key=lambda x: x[0].ind)
    for i in A:
        print('"'+str(worker_tag[i[0].ind])+'"','should be given','"'+str(task_tag[i[1].ind])+'"')