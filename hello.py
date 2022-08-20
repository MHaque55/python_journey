class Student:
    name = [0 for  i in range(5)]
    age = [0 for  i in range(5)]
    num = 0

Student.num = 0
i = 0
while Student.num < 5:
    student_name = input('Student\'s name: ')
    while i < Student.num:
        if student_name == Student.name[i]:
            print('Name already exist')
            break
        i = i + 1
    if i == Student.num:
        Student.name[Student.num] = student_name
        student_age = input('Enter his\her age: ')
        Student.age[Student.num] = student_age
        Student.num = Student.num + 1

for n in range(Student.num):
    print(Student.name[n] + ',age:', Student.age[n])