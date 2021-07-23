inputtxt = open(r"F:\CSE 221\Lab Assignments\Week 2\input_2.txt","r")
result = open(r"F:\CSE 221\Lab Assignments\Week 2\output_2.txt","w")
def selectionSort(arr):
    for i in range(len(arr)-1):
        mini = i
        for j in range(i+1,len(arr)):
            if arr[mini] > arr[j]:
                mini  = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr
line = inputtxt.readline()
n = [0]*2
j = 0
for i in line.split():
    if i.isdigit():
        n[j] = int(i)
        j += 1
array = [0]*n[0]
line = inputtxt.readline()
k = 0
for i in line.split():
    if i.isdigit():
        array[k]= int(i)
        k += 1

r = selectionSort(array)
for t in range(len(r)-1):
    if t > n[1]-1:
        break
    result.write(str(r[t])+' ')
inputtxt.close()
result.close()

