class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
class MyList:
    def __init__ (self,data = None):
        self.head=None
        last=None
        for i in data:
            node = Node(i)
            if self.head is None:
                self.head=node
                last=node
            else:
                last.next=node
                last=node
    def selectandsort(self):
        item = self.head
        index = None 
        if self.head == None:
            return 
        else: 
            while item != None :
                index = item.next 
                while index != None: 
                    if item.data > index.data:
                        temp = item.data 
                        item.data = index.data 
                        index.data = temp 
                    index = index.next 
                item = item.next 
    def showList(self):
        if self.head is None:
            print("The List is empty")
        else:
            n=self.head
        while n is not None:
            print (n.data)
            n=n.next
list = [3,1,2,5,6,7,4]
list1 = MyList(list)
list1.selectandsort()
list1.showList()