array = open(r"F:\CSE 221\Lab Assignments\Week 2\input_1.txt","r")
result = open(r"F:\CSE 221\Lab Assignments\Week 2\output_1.txt","w")
# we know best case scenario for any kind of sort is to have an array already sorted.
def bubbleSort(arr):
    for i in range(len(arr)-1):
        swap = True         #So, We take a boolean variables that remains true if no kinds of sort has occured.
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swap = False #Here, we are iterating swap as false for the sort has occured
        if swap== True: # and Finally, has no kind of swap has occur we can come to conclusion that array has already sorted. 
                        #Thus, the loops get terminated and we have best case scenario for the code.
            break
    print(arr)
    return arr
n = int(array.readline())
arr = [0]*5
inputtxt = array.readline()
j = 0
for i in inputtxt.split():
    if i.isdigit():
        arr[j] = int(i)
        print(i)
        j += 1
t = bubbleSort(arr)
result.write(str(t))
array.close()
result.close()
