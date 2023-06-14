from classes import *

def Output(Asg:set[tuple[worker,task]]):
    for i in Asg:
        print('Worker',i[0].ind,'to task',i[1].ind)