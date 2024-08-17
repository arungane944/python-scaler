budget = [100, 150, 200, 90, 100]
students = ["Rajini", "Kamal", "Ajith"]
# count function
print(budget.count(100))
print(budget.count(10))

#index 
print(budget.index(150))
print(students.index("Ajith"))

#drop
students.remove("Kamal")
print(students)

#sort
budget.sort()
students.sort()

print(budget)
print(students)

#insert

students.insert(0, "siva")
print(students)

# append

students.append("sethupathi")
print(students)