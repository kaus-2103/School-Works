class Node:
    def __init__ (self,data):
        self.item = data
        self.ref = None
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
                last.ref=node
                last=node
    def showList(self):
        if self.head is None:
            print("The List is empty")
        else:
            n=self.head
            while n is not None:
                print (n.item)
                n=n.ref
    def LinkedList(self):
        i = self.head
        while i is not None:
            j = self.head
            while j is not None:
                j.item = i.item
                j = j.ref
            i = i.ref
    def isEmpty(self):
        if self.head is None:
            return True;
        else:
            return False;
    def clearself(self):
        i = self.head
        while i is not None:
            self.head = None
            i = i.ref
    def insert(self, newElement):
        if self.head is None:
            self.item = newElement
        if self.head is None:
            print("The List is empty")
        else:
            n=self.head
            while n is not None:
                print (n.item)
                n=n.ref
    def insert1(self, newElement, index):
        c = self.head
        i = 0
        while c is not None :
            i = i + 1
            if c>index:
                print("Out of Index")
            else:
                self.item = newElement
            c = c.ref
    def remove(self, deletekey):
            i = self.head
            while i is not None:
                if (i.item == deletekey):
                    i.item = None
                i = i.ref
            i=self.head
            while i is not None:
                print (i.item)
                i=i.ref
s = MyList([1,2,3,4])
s.insert(2)
s.showList()

