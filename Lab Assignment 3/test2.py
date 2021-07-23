class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    #  Creation of Circular Doubly Linked List
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
    def showList(self):
        if self.head is None:
            print("The List is empty")
        else:
            n=self.head
            while n is not None:
                print (n.value)
                n=n.next
s = CircularDoublyLinkedList()
s.createCDLL([10,20,30,40,50])
s.showList()