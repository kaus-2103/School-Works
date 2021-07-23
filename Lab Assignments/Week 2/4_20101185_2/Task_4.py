inputtxt = open(r"F:\CSE 221\Lab Assignments\Week 2\input_4.txt","r")
result = open(r"F:\CSE 221\Lab Assignments\Week 2\output_4.txt","w")
def merge(arr):
    if len(arr)> 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        print(left)
        print(right)
        merge(left)
        merge(right)
        i= j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] =  left [i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] =  right[j]
            j += 1
            k += 1
    return arr
n = int(inputtxt.readline())
arr1 = [0]*n
array = inputtxt.readline()
j= 0
for i in array.split():
    arr1[j] = int(i)
    j +=1
print(arr1)
inputtxt.close()
r = merge(arr1)
result.write(str(r))
