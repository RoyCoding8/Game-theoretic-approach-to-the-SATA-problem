from Gen_input import *
import itertools as itr

def generate_all_combinations(lists):
    subsets = list(itr.product(*lists))
    return subsets

def search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

def calculate_probabilities(all_subsets,sub,prob):
    l =[]
    for subset in all_subsets:
        p=1
        for i in range(len(subset)):
            x = search(sub[i],subset[i])
            p *= prob[i][x]
        l.append(p)
    return l

def get_subsets(arr):
    lst,prob=[],[]
    for i in arr:
        lst.append(i[1])
        prob.append(i[0])
    subsets = []
    prob_subsets = []
    product = 1
    for i in prob:
        product *= (1-i)
    n = len(lst)
    for i in range(1<<n):
        subset = []
        p=product
        for j in range(n):
            if (i>>j) & 1:
                subset.append(lst[j])
                p *= prob[j]
                p /= (1-prob[j])
        subsets.append(subset)
        prob_subsets.append(round(p,2))
    return subsets,prob_subsets

sub = []
prob_subsets = []

for i in range(1,len(ws_incmp)):
    tmp = get_subsets(ws_incmp[i])
    sub.append(tmp[0])
    prob_subsets.append(tmp[1])

all_subsets = generate_all_combinations(sub)
all_prob = calculate_probabilities(all_subsets,sub,prob_subsets)