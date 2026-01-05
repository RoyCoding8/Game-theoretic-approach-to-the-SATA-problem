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

import random

def sample_skills(ws_incmp):
    # ws_incmp is a list of lists.
    # index i corresponds to worker i (1-indexed usually, so index 0 empty or unused?)
    # each element is a list of tuples (probability, skill)
    
    sampled_skills = {} # Map worker_index -> list of skills
    
    for i in range(1, len(ws_incmp)): # Assuming 1-based indexing as per Gen_input
        skills = []
        for prob, skill in ws_incmp[i]:
            if random.random() < prob:
                skills.append(skill)
        sampled_skills[i] = skills
        
    return sampled_skills