def Hashtable(list):
    list = list
    len1 = len(list)
    array = [0]*9
    for i in list:
        counter_d = 0
        counter_c = 0
        value = 0
        for j in i:
            if (j >='A' and j <='Z') or (j >='a' and j <='z'):
                if j !='A' and j !='a' and j !='E' and j !='e' and j !='I' and j !='i' and j !='O' and j !='o' and j !='U' and j !='u'   :
                    counter_c = counter_c + 1
        for k in i:
            if k >='0' and k <='9':
                k = int(k)
                counter_d = counter_d + k
        value = (counter_c*24+(counter_d))%9
        l1 = linearprobe(i,value,len1,array)
def linearprobe(i,value,len1,array):
    if value == len1:
        value = 0
    if array[value] != 0:
        return (i,value+1,len1)
    else:
        array[value]=i
    print(array)
list = ['78221AQ','A1m','COD12','Bruh']
list1 = Hashtable(list)
