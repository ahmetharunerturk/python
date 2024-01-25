import datetime
today = datetime.date.today()
year = today.year

print("Your name: ")
name = input()

print("Your age: ")
age = int(input())
dateOfBirth = year - age

print(f"{name} 100 yaşında olacağınız tarih: {dateOfBirth+100}")

