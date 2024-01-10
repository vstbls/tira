from collections import namedtuple
from tkinter import N

def rec(node):
    if not node.left and not node.right:
        return [1], 0
    if not node.left:
        r_list, r_sum = rec(node.right)
        return [i+1 for i in r_list], r_sum
    if not node.right:
        l_list, l_sum = rec(node.left)
        return [i+1 for i in l_list], l_sum
    l_list, l_sum = rec(node.left)
    r_list, r_sum = rec(node.right)
    sum = l_sum+r_sum
    for l in l_list:
        for r in r_list:
            sum += l+r
    return [i+1 for i in l_list+r_list], sum

def count(node):
    return rec(node)[1]

def count_leaves(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaves(node.left)+count_leaves(node.right)

def count_paths(node,n):
    if not node:
        return (0,0)
    left = count_paths(node.left,n)
    right = count_paths(node.right,n)
    leaves = left[1]+right[1]
    if not node.left and not node.right:
        leaves += 1
    return (left[0]+right[0]+leaves*(n-leaves),leaves)

def count2(node):
    n = count_leaves(node)
    return count_paths(node,n)[0]

def rec2(node):
    if node.left == None and node.right == None:
        return 1,0,1 # lehtien määrä, summa tähän asti, matkat lehdille
    if node.left and node.right:
        l = rec2(node.left)
        r = rec2(node.right)
        return l[0]+r[0], l[1]+r[1] + l[0]*r[2] + l[2]*r[0], l[2]+r[2] + l[0]+r[0]
    if node.left:
        n = rec2(node.left)
    else:
        n = rec2(node.right)
    return n[0],n[1],n[2]+n[0]

def count3(node):
    return rec2(node)[1]

from time import time

if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(Node(None,None),Node(Node(None,None),Node(None,None)))
    tree2 = Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=None))
    center = Node(None, None)
    for i in range(15):
        left = center
        right = center
        center = Node(left, right)
    n = 1
    t1 = time()
    for i in range(n):
        count(center)
    t2 = time()
    print(t2-t1)
    for i in range(n):
        count2(center)
    t3 = time()
    print(t3-t2)
    for i in range(n):
        count3(center)
    t4 = time()
    print(t4-t3)
    print(t2-t1,t3-t2,t4-t3)