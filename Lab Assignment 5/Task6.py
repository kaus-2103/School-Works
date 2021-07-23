def adder(node):
    if node.next == None:
        return node
    else:
        return node.data+adder(node.next)