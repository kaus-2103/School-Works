def vowels(x):
    count=0
    vowel=["a","e","i","o","u","A","E","I","O","U"]
    j=[]
    for i in x:
        if i in vowel:
            count+=1
            j.append(i)
    print("Vowels = ",j,end=" ,")


    return count


name=input("Enter the name:")
print("Total number of vowels=",vowels(name))