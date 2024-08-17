# Since arguments are specified by name, you can pass them in any order.

def introduce(name, age, city):
    print(f"My name is {name}, I am {age} years old, and I live in {city}.")

# Using keyword arguments
introduce(name="Alice", age=25, city="New York")

# You can change the order of the arguments
introduce(city="Los Angeles", age=30, name="Bob")
