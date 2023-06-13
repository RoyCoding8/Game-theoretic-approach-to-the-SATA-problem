from classes import *

def Output(Asg:list[tuple[worker,task]]):
    for i in range(len(Asg)):
        w=Asg[i][0]
        t=Asg[i][1]
        print('Worker',w.ind,'to task',t.ind)