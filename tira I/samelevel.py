from collections import namedtuple

def rec(node, level, current):
    if not node:
        return 0
    if current == level:
        return 1
    return rec(node.left, level, current+1) + rec(node.right, level, current+1)

def count(node, level):
    return rec(node, level, 1)

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree,1)) # 1
    print(count(tree,2)) # 1
    print(count(tree,3)) # 2
    print(count(tree,4)) # 0