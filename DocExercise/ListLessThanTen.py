a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []

for num in a:
    if 5 > num:
        newList.append(num)

print(newList)

#Extra

print("Number: ")
number = int(input())

UserList = []

for i in a:
    if number > i:
        UserList.append(i)

print(UserList)