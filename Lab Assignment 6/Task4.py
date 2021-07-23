class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
class MyList:
    def __init__ (self,data = None):
        self.head=None
        last=None
        self.count = 0
        for i in data:
            node = Node(i)
            if self.head is None:
                self.head=node
                last=node
            else:
                last.next=node
                last=node
            self.count =  self.count + 1
    def bubbleandsort(self):
        for i in range(self.count-1):
            item = self.head
            next = item.next
            temp = None
            while next:
                if item.data > next.data:
                    if temp == None:
                        temp = item.next 
                        next = next.next 
                        temp.next = item 
                        item.next = next
                        self.head = temp 
                    else: 
                        temp2 = next 
                        next = next.next 
                        temp.next = item.next 
                        temp = temp2 
                        temp2.next = item 
                        item.next = next 
                else: 
                    temp = item 
                    item = next 
                    next = next.next
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
list1.bubbleandsort()
list1.showList()