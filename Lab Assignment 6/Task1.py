def min(a,i,j) :
    if i == j :
        return i
    if a[i] < a[min(a,i+1,j)]:
        return i
    else:
        return min(a,i+1,j)
def selectandsort(a,i,location = 0) :
    if location == i :
        return -1
    min(a,location,i-1)
    if min(a,location,i-1) != location :
        temp = a[min(a,location,i-1)]
        a[min(a,location,i-1)] = a[location]
        a[location] = temp
    selectandsort(a,i,location+1)
arr = [3,1,2,5,6,7,4]
i = len(arr)
selectandsort(arr,i)
for i in arr:
    print(i,end=' ')
