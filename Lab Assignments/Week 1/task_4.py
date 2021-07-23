import numpy as np
inpt = open(r"F:\CSE 221\Assignment 1\input4.txt","r")
output = open(r"F:\CSE 221\Assignment 1\output4.txt","w")
n = int(inpt.readline())
M = inpt.readline()
A = []
B = []
for j in range(n):
    a = []
    for i in M.split():
        a.append(int(i))
    A.append(a)
    M = inpt.readline()
for j in range(n):
    a = []
    M = inpt.readline()
    for i in M.split():
        a.append(int(i))
    B.append(a)
inpt.close()
C = np.zeros((n,n))
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k]*B[k][j]
            
for i in C:
    output.write(str(i)+'\n')
