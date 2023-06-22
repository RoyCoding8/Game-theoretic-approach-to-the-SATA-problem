from classes import *
from Gen_input import *

def Output(Asg:set[tuple[worker,task]]):
    for i in Asg:
        # print('"'+str(worker_tag[i[0].ind])+'"','should be given','"'+str(task_tag[i[1].ind])+'"')
        print(i[0].ind,i[1].ind)