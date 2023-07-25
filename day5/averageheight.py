'''

fruits = ["Apple","orange", "BANANA"]

for fruit in fruits:
    print(fruit)

'''

student_heights = input("student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height =0
x=0
for height in student_heights:
  total_height+=height
  x+=1
avg=total_height/x
print(round(avg))