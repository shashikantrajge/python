
number = int (input ('enther the number of student'))
print (number)
i = 0
A = []
while i < number:
    age = int(input("Enter age: "))
    print(age)
    A.insert(i,age)
    #A.append(age)
    #A.extend(age)
    i = i+1

print(A)

