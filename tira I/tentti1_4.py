def larger_numbers(node: Node, x: int):
    if not node:
        return 0
    n = larger_numbers(node.left) + larger_numbers(node.right)
    if node.value > x:
        return n+1
    return n

def largest_leaf(node: Node):
    while(node.right and node.left):
        if node.right:
            node = node.right
        else:
            node = node.left
    return node.key
    