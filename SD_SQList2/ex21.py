def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b
def subtract(a,b):
    print(f"SUBTRACT {a} - {b}")
    return a - b
def multiply(a,b):
    print(f"MUTIPLY {a} * {b}")
    return a * b
def divide(a,b):
    print(f"DIVIDE {a} / {b}")
    return a / b
    #函数返回的是一个数，即运算后的结果


print("Let's do some math with just functions!")


age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)


print(f"Age: {age},Height: {height},Weight: {weight},IQ: {iq}")
#print("age: ",age)
#A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print("That becomes: ", what ,"Can you do it by hand?")
