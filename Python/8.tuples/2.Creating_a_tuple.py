students = ()
print(type(students))

#(or)

students_1 = tuple()
print(type(students_1))

t1 = (1) # ? Very important. Here considered as oprations
print(type(t1))

t2 = (1,2)
print(type(t2))

t3 = (1,) # Very important
print(type(t3))



course = tuple('python')
print(type(course))
print(course)

course1 = ('python')
print(type(course1))
print(course1)



courses = ('python', 'istio')
for course in courses:
    print(course)



t = ([1,2],[3,4])
print(type(t))