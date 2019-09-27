i = 0

l = input("input loop numbers")
def while_loop(l,i) :

    l=int(l)#python中input键入的类型默认为str
    numbers = []
    while i < l :
        print(f"At the top i is {i}")
        numbers.append(i)


        i+=1
        print("Numbers now: ",numbers)
        print(f"At the bottom i is {i}")
    print("The numbers: ")


    for num in numbers :
        print(num)


while_loop(l,i)
#猜测str默认用list 方法转化为列表了
numbers = input("try")
for num in numbers :
    print(f"the num : {num}")
