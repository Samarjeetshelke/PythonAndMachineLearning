students = [
     ("Rushi",18,"C"),
     ("Riya",21,"B"),
    ("Samarjeet",21,"A")
]

print(students)    

students.append(("Aniket",20,"A++"))

print(students)

for student in students:
    name,age,grade = student
    print(f"Name:{name},Age:{age},Grade:{grade}")
    
    
#find the student with perticular grade
grade="A++"

print([student[0] for student in students if student[2]=="A++"])


#sort the student according to greads
print(sorted(students,key=lambda student:student[2]))

