def insertandsort(list,i):
    if i<1:
        return None
    insertandsort(list,i-1)
    temp = list[i-1]
    j = i-2
    while(j>=0 and list[j]>temp):
        list[j+1] = list[j]
        j = j-1
    list[j+1] = temp
def binary_search(list,min,max,i):
    if max>=min:
        med = (max+min)//2
        if list[med] == i:
            return med
        elif list[med] > i:
            return binary_search(list,min,med-1,i)
        else:
            return binary_search(list,med+1,max,i)
    else:
        return -1
list = [3,1,2,5,6,7,4]
i = 1
insertandsort(list,len(list))
s = binary_search(list,0,len(list)-1,i)
if s != -1:
    print(s)
else:
    print(None)