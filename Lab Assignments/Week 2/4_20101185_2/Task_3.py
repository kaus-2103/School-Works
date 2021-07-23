inputtxt = open(r"F:\CSE 221\Lab Assignments\Week 2\input_3.txt","r")
result = open(r"F:\CSE 221\Lab Assignments\Week 2\output_3.txt","w")
def insertionSort(arr1,arr2):
    for i in range(len(arr1)-1):
        temp = arr1[i+1]
        temp2 = arr2[i+1]
        j = i
        for j in range(i,0,-1):
            if arr2[j] < temp2:
                arr1[j+1] = arr1[j]
                arr2[j+1] = arr2[j]
            else: 
                break
        arr1[j+1] = temp
        arr2[j+1] = temp2
    return arr1
    
n = int(inputtxt.readline())
arr1 = [0]*n
arr2 = [0]*n
array = inputtxt.readline()
j= 0
for i in array.split():
    if i.isdigit():
        arr1[j] = int(i)
        j +=1
k =0
array = inputtxt.readline()
for i in array.split():
    if i.isdigit():
        arr2[k] = int(i)
        k +=1
    
inputtxt.close()
r = insertionSort(arr1,arr2)
result.write(str(r))
result.close()

