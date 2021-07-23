class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
def getNode():
    return(Node(0))   
class DoublyList:
    def __init__(self,data ):
        self.head = None
        self.tail = None
        for i in data:
            item = Node(i)
            item.prev = self.tail
            if self.tail == None:
                self.head = item
                self.tail = item
                item.next = None  
            else:
                self.tail.next = item
                self.next = None
                self.tail = item
    def showList(self):
        if self.head is None:
            print("The List is empty")
        else:
            n=self.head
            while n is not None:
                print ("-->",n.data)
                n=n.next
    def insert(self,data):
        item = Node(data)
        item.prev = self.tail
        l = data
        b = self.search(l)
        if b == False:
            if self.tail == None:
                self.head = item
                self.tail = item 
                item.next = None
            else:
                self.tail.next = item
                item.next = None
                self.tail = item 
        else:
            return 
    def insert1(self,newElement,index):
        b = self.search(newElement)
        if b == False:
            t=self.head
            count=0
            while count <index:
                t=t.next
                count=count+1
            t=self.head
            item=getNode()
            item=Node(newElement)
            i=t.next
            j=t
            t.next=item
            t=t.next
            t.prev=j
            t.next=i
            j=t
            t=t.next
            t.prev=j
    def remove(self,index):
            i = self.head
            c = index-1
            c1 = 0
            while i is not None:
                if (c==c1 ):
                    i.data = None
                c1 = c1 +1
                i = i.next
            i=self.head
            while i is not None:
                print (i.data)
                i=i.next  
    def removekey(self, deletekey):
            i = self.head
            while i is not None:
                if (i.data == deletekey):
                    i.data = None
                i = i.next
            i=self.head
            while i is not None:
                print (i.data)
                i=i.next    
    def search(self, data):
            t = self.head
            while t:
                if t.data == data:
                    return True
                if t == self.tail:
                    return False
                t = t.next
s = DoublyList([10,20,30,40,50])
s.insert(50)
s.showList()
