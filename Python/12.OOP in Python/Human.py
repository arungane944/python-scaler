class Human:

# !! Accessing instance attributes with self
    
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def greeting(self): 
        print(f"Hey my name is {self.name}. Good Morning!!!")

    def celebrate_birthday(self):
    # Accessing and modifying instance attributes
        self.age += 1
        print(f"Happy Birthday! Now you are {self.age} years old.")


arun = Human("Arun", 25, "Cricket")
arun.greeting()
arun.celebrate_birthday()
print(f"My name is {arun.name}")