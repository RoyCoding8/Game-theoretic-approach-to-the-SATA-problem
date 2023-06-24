from Start import *

# ----------------------Now using synthetic dataset to study the effect worker cost-------------------------

from Input_t0 import *
from Input_w0 import *

T,W=[],[]
worker_cost = [5]*(m+1)
assignments_cost_greedy,sat_cost_greedy = [],[]
assignments_cost_gt,sat_cost_gt = [],[]

# worker cost = 5
print('---------------------Worker cost = 5---------------------')
input_tasks(n,T)
input_workers(m,W)
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_cost_greedy.append(len(Asg))
sat_cost_greedy.append(s)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_cost_gt.append(len(Asg))
sat_cost_gt.append(s)

# worker cost = 7
print('---------------------Worker cost = 7---------------------')
W=[]
worker_cost = [7]*(m+1)
input_workers(m,W)
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_cost_greedy.append(len(Asg))
sat_cost_greedy.append(s)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_cost_gt.append(len(Asg))
sat_cost_gt.append(s)

# worker cost = 8
print('---------------------Worker cost = 8---------------------')
W=[]
worker_cost = [8]*(m+1)
input_workers(m,W)
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_cost_greedy.append(len(Asg))
sat_cost_greedy.append(s)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_cost_gt.append(len(Asg))
sat_cost_gt.append(s)

# worker cost = 10
print('---------------------Worker cost = 10---------------------')
W=[]
worker_cost = [10]*(m+1)
input_workers(m,W)
Asg=greedy(T,W)[0]
s = Cal_Sat(Asg)
print('No of assignments by CAG Algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
assignments_cost_greedy.append(len(Asg))
sat_cost_greedy.append(s)

Asg=GT_algo(T,W)
s = Cal_Sat(Asg)
print('No of assignments by GT algorithm:',len(Asg))
print('Satisfaction score of the assignment:',s)
print('--------------------------------------------------')
assignments_cost_gt.append(len(Asg))
sat_cost_gt.append(s)

plt.plot([5,7,8,10],assignments_cost_greedy,label='CAG')
plt.plot([5,7,8,10],assignments_cost_gt,label='GT')
plt.xlabel('Worker cost')
plt.ylabel('No of assignments')
plt.title('No of assignments vs Worker cost')
plt.legend()
plt.show()

plt.plot([5,7,8,10],sat_cost_greedy,label='CAG')
plt.plot([5,7,8,10],sat_cost_gt,label='GT')
plt.xlabel('Worker cost')
plt.ylabel('Satisfaction score')
plt.title('Satisfaction score vs Worker cost')
plt.legend()
plt.show()