x=15 # global variable

def my_function():
    x = 10  # Local variable
    print(x)

my_function()
print(x)  # This will raise an error because x is not defined outside the function
