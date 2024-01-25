height = input('height m: ')
weight = input('weight kg: ')

bmi = int(weight)/ (float(height)**2)

if bmi<18.5:
    print("underweight")
elif bmi>18.5 and bmi<25:
    print("normal weight")
elif bmi>25 and bmi<30:
    print("slightly overweight")
elif bmi>30 and bmi<35:
    print("obese")   
elif bmi>35:
    print("clinically obese")    
