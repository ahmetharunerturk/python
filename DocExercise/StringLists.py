inp = input("palindrome or not?: ")

word = inp.lower()

lenWorth = len(word)
palindrome=True

for i in range(0, lenWorth):
    j = lenWorth - 1 - i
    if word[i] != word[j]:
        palindrome = False
        break

if palindrome == True:
    print("It's a palindrome",inp)
else:
    print("It isnt a palindrome")