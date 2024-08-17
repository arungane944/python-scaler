students_a = ["Rajini", "Kamal", "Ajith"]
students_b = ["shankar", "Kamal", "vetrimaran", "rajamouli"]
new_student = "pradeep"


# append

#students_a.append(students_b)
#print(students_a)

# extend -> Internally iterate the object and add one by one
students_a.extend(students_b)
print(students_a)

students_a.extend(new_student) # internally it iterating the string chars and added in list
print(students_a)

for char in new_student:
    print(char)