def add(a,b):
    return a+b

print(add(5,10))

#################################
func = lambda a, b : a+b

print(func(3,4))

#################################

def larger(a,b):
    if(a>b):
        return a
    else:
        return b

print(larger(10,20))

####################################

larger_lambda = lambda a,b : a if a>b else b

print(larger_lambda(10,20))
