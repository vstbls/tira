from collections import namedtuple

def rec(node):
    if not node:
        return 0, 0
    left, dleft = rec(node.left)
    right, dright = rec(node.right)
    d = abs(left-right)
    return left+right + 1, max(dleft, dright, d)

def diff(node):
    return rec(node)[1]

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(diff(tree)) # 3