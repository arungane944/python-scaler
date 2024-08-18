## arbitrary arguments allow you to pass a variable number of arguments to a function. 

def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")  # Output: Hello, Alice! Hello, Bob! Hello, Charlie!


## !! The **kwargs syntax allows a function to accept any number of keyword arguments, which are then accessible as a dictionary 
# !! inside the function.

def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, country="USA")


def example_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example_function(1, 2, 3, name="Alice", age=30)
