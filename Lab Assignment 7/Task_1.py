class KeyIndex:
    def __init__(self,list):
        self.list = list
        self.len = len(list)
        max = self.list[0]
        min = 0
        for i in self.list:
            if i < 0:
                min = i
                for j in self.list:
                    if j < min :
                        min = j 
        for i in range(self.len):
            self.list[i] = self.list[i]+(-1*min)
        for i in range(self.len):
            if self.list[i]>max:
                max = self.list[i]
        aux  = [0]*(max+1)
        for i in self.list:
            counter = 0
            while counter < max+1:
                if counter == i:
                    aux[counter] = aux[counter] + 1
                counter = counter+1
        print(aux)
        print(self.list)
    def search(self,value):
        self.value = value 
        c = 0
        for i in self.list:
            if i == self.value:
                c = c+1
            else:
                c = c
        if c >= 1:
            print("The value is present in the list.")
        else:
            print("The value is not present in the list.")
    def sort(self):
        for i in range (self.len):
            for j in range (self.len):
                if self.list[i]<self.list[j]:
                    t = self.list[j]
                    self.list[j] = self.list[i]
                    self.list[i] = t
                    print("T = ",t,"J = ",j,"i = ",i)
        print(self.list)


list = [-1,5,-9,5,-9,0,8,-1]
list1 = KeyIndex(list)
list1.search(0)
list1.sort()