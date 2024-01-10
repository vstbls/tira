from collections import namedtuple
 
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
 
if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(Node(None,None),Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 8