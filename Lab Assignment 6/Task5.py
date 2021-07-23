class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None 
def DoublyList(item,data):
    node = Node(0)
    node.data = data 
    node.next = item
    node.prev = None 
    if item != None:
        item.prev = node
    item = node
    return item
def sorted(head,node):
    item = None
    if head == None :
        head = node 
    elif head.data >= node.data :
        node.next = head 
        node.next.prev = node 
        head = node 
    else : 
        item = head 
        while item.next != None and item.next.data < node.data :
            item = item.next 
        node.next = item.next 
        if item.next != None:
            node.next.prev = node 
        item.next = node 
        node.prev = item 
    return head 
def insertion(head):
    sort = None 
    item = head 
    while item != None :
        next = item.next 
        item.prev = None 
        item.next = None 
        sort = sorted(sort,item)
        item = next 
    head = sort 
    return head 
def showList(item):
    while item is not None:
        print(item.data)
        item.next
list = [3,1,2,5,6,7,4]
i = 0
list1 = None
j = 0
while j < len(list):
    list1 = DoublyList(list1,list[j])
    j = j+1
insertion(list1)
#showList(list1)