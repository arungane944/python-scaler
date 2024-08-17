# default arguments

def greet(name="Guest", greeting="Hello"):
    print(f"{greeting}, {name}!")

# Calling the function without arguments uses the default values
greet()  # Output: Hello, Guest!

# Providing only the first argument, the second uses its default value
greet("Alice")  # Output: Hello, Alice!

# Providing both arguments
greet("Bob", "Welcome")  # Output: Welcome, Bob!

# Changing only the greeting by using a named argument
greet(greeting="Hi")  # Output: Hi, Guest!

######################

def introduce(name, age, country="USA"):
    print(f"My name is {name}, I am {age} years old, and I am from {country}.")

##Non-default arguments must be provided by the caller. In the above example, name and age are non-default arguments, so you must supply them when calling the function.
    
introduce("Alice", 30)  # Output: My name is Alice, I am 30 years old, and I am from USA.