number = int(input("Enter a number: "))

x = range(1,number+1)

for elem in x:
    if number % elem  == 0:
        print(elem)