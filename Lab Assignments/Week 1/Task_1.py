File_object = open(r"F:\CSE 221\Assignment 1\input.txt","r")
output = open(r"F:\CSE 221\Assignment 1\output.txt","w")
record = open(r"F:\CSE 221\Assignment 1\record.txt","w")
l = File_object.readline()
num = 0
odd = 0
even = 0
non = 0
palindrome = 0
non_palindrome = 0
count = 0
pri = ""
pris = ""
while  l:
    for i in l.split():
        if  i.isdigit():
            i = int (i)
            if i % 2 == 0:
                even = even + 1
                pri = str(i) +" has a even parity and "
                output.write(pri)
            else :
                odd = odd +1
                pri = str(i)+" has a odd parity and "
                output.write(pri)
        elif i.isalpha():
            N = len(i)
            j = 0
            while j  < N/ 2:
                if i[j] == i[N-1-j]:
                    palindrome = palindrome + 1
                    pris = str(i)+" is a palindrome .\n"
                    output.write(pris)
                    break
                else:
                    non_palindrome =  non_palindrome + 1
                    pris = str(i)+" is not a palindrome .\n"
                    output.write(pris)
                    break
                j = j + 1 
        else:
            pri = str(i) +" can not parity and "
            non = non +1
            output.write(pri)
    count = count + 1
    l = File_object.readline()
print(odd,even,non,non_palindrome,palindrome)
record.write("Percentage of odd parity: "+ str ((odd/count)*100)+" %.\n")
record.write("Percentage of even parity: "+ str ((even/count)*100)+" %.\n")
record.write("Percentage of no parity: "+ str ((non/count)*100)+" %.\n")
record.write("Percentage of palindrome parity: "+ str ((palindrome/count)*100)+" %.\n")
record.write("Percentage of odd parity: "+ str ((non_palindrome/count)*100)+" %.\n")
File_object.close()
output.close()
record.close()