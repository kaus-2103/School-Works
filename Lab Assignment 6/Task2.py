def insertandsort(list,i):
    if i<1:
        return None
    insertandsort(list,i-1)
    temp = list[i-1]
    j = i-2
    while j>=0 and list[j]>temp:
        list[j+1] = list[j]
        j = j-1
    list[j+1] = temp
list = [3,1,2,5,6,7,4]
insertandsort(list,len(list))
print(list)
