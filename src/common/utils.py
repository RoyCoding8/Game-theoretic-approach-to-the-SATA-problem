from .classes import *
from .distance import *

def set_itr(l1, l2):
    s1, s2 = set(l1), set(l2)
    return [i for i in s1 if i in s2]

def csore(u, v):
    b, w = 0.5, 0.01
    itr = len(set_itr(u.task_set, v.task_set))
    unon = len(u.task_set) + len(v.task_set) - itr
    if unon == 0:
        return b * w
    return b * w + (1 - b) * itr / unon

def csat(W):
    n = len(W)
    if n <= 1:
        return 0
    total = 0
    for i in range(n):
        for j in range(i):
            total += csore(W[i], W[j])
    return 2 * total / (n - 1)

def psat(t, W):
    total = 0
    for w in W:
        dist = calculate_distance(t.latitude, t.longitude, w.latitude, w.longitude)
        total += dist * w.cost
    return t.budget - total

def sat(t, W):
    a, p_max, c_max = 0.5, 100000, 10000
    return a * psat(t, W) / p_max + (1 - a) * csat(W) / c_max

def check_worker(t, w):
    if not set_itr(t.K_req, w.K):
        return False
    dist = calculate_distance(t.latitude, t.longitude, w.latitude, w.longitude)
    return dist <= w.r

def check_validity(t, W):
    if psat(t, W) < 0:
        return False
    covered = set()
    for w in W:
        covered.update(w.K)
    if not all(req in covered for req in t.K_req):
        return False
    n = len(W)
    for i in range(n):
        for j in range(i + 1, n):
            if set_itr(W[i].K, W[j].K):
                return False
    return True

def check_CWS(t, W):
    for w in W:
        if not check_worker(t, w):
            return False
    return check_validity(t, W)

def rm_el(a, w):
    return [i for i in a if i != w]

def dif_psat(t, w):
    dist = calculate_distance(t.latitude, t.longitude, w.latitude, w.longitude)
    return -w.cost * dist

def cop_sum(W, w):
    return sum(csore(i, w) for i in W)

def dif_sat(dpsat, dcsat):
    a, p_max, c_max = 0.5, 100000, 10000
    return a * dpsat / p_max + (1 - a) * dcsat / c_max