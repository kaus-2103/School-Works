def printlist(n):
    if len(n)==1:
        return
    return print(n,printlist(n[1:]))
    
list = printlist([1,2,3,4,5,6])