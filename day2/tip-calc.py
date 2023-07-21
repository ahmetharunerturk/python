'''
data types

string: 'Hello' print("Hello"[1])
int: 1000 or 123_456_678
float: 1123.09
boolean: 1 or 0

type()

int_sayi = int(sayi)
toplam = int_sayi[0] + int_sayi[1]
print(toplam)

sayi = input('Sayı giriniz: ')
firts_number = int(sayi[0])
second_number = int(sayi[1])
print(firts_number+second_number)

3%2 == 1

score = 1
print(f"your score is {score}")


'''

print("welcome to the tip calc")

total_bill = input("what was the total bill? ")
tip = input("what percentage tip? 10,12, or 15? ")
people = input("how many people to split the bill? ")

bill_with_tipp = int(total_bill)+(int(total_bill)*int(tip)/100)
bill_per_person = bill_with_tipp/int(people)

print(f"Each person should pay: {bill_per_person}")






