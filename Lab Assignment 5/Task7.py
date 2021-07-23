def reverse(node):
    if node.next == None:
        return node
    node_temp= reverse(node.next)
    node.next.next = node
    node.next = None
    return node_temp