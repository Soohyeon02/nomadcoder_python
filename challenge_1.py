def plus(a,b):
    return int(a) + int(b)

def minus(a,b):
    return int(a) - int(b)

def times(a,b):
    return int(a) * int(b)

def division(a,b):
    return int(a) / int(b)

def negation(a):
    return -int(a)

def power(a,b):
    return int(a) ** int(b)

def remainder(a,b):
    return int(a) % int(b)

print(plus(3,"5"))
print(minus("4",1))
print(times("12",2))
print(division("15","3"))
print(negation("-6"))
print(power("12",2))
print(remainder("21","3"))