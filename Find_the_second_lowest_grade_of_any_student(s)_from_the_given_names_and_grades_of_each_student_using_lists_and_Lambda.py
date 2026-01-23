# Python: Find the second lowest grade of any student(s) from the given names and grades of each student using lists and Lambda



students = []
sec_name = []
second_low = 0

n = int(input('Enter number of students : '))

for _ in range(n):
    s_name = input('Name : ')
    score = int(input('Grade : '))
    students.append([s_name,score])
    
print(students)

order = sorted(students,key = lambda x:int(x[1]))

for i in range(n):
    
    if order[i][1] !=order[0][1]:
        second_low = order[i][1]
        break
        
sec_student_name = [x[0] for x in order if x[1]==second_low]

sec_student_name.sort()
print("Second lowest grade: ", second_low)    
print(sec_student_name)