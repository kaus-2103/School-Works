class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            item = Node(data)
            item.next = self.head
            self.head = item
    def pop(self):
        if self.head == None:
            return None
        else:
            item = self.head
            self.head = self.head.next 
            item.next = None 
            return item.data

list = "([])"    
counter = 0
stack = Stack()
l = 0
k = 0
m = 0
for i in list:
    if i in ["(","{","["]:
        stack.push(i)
    else:
        if stack.head==None and i==')':
            print("Missing ( expected at",counter+1)
            print("The expression is incorrect.")
            break
        if stack.head==None and i=='{':
            print("Missing { expected at",counter+1)
            print("The expression is incorrect.")
            break
        if stack.head==None and '[':
            print("Missing [ expected at",counter+1)
            print("The expression is incorrect.")
            break
        c = stack.pop()
        if c =='(':
            l = 0
            for j in list:
                if j ==")":
                    l = l+1
            if l == 0:
                print("The expression ) is missing in",counter)
                break
        if c == '{':
            k = 0
            for j in list:
                if j =="}":
                    k=k+1
            if k == 0:
                print("The expression } is missing in ",counter)
                break 
        if c =='[':
            m = 0
            for j in list:
                if j =="]":
                    m = m+1
            if m==0:
                print("The expression ] is missing in ",counter)
                break
    counter = counter + 1
if stack.head==None and (l>0):
    print("The Expression is correct.")
elif stack.head==None and (k>0):
    print("The Expression is correct.")
elif stack.head==None and (m>0):
    print("The Expression is correct.")
else:
    print("Expected",i,"at",counter)

