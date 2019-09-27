types_of_people=10
x=f"there {types_of_people} types of people."
binary="binary"
do_not="don't"
y=f"Those who know {binary} and those who {do_not}."
#print(f"{do_not}") f使用于双引号中string字符转换，配合｛｝使用
print(x)#print可以直接打印出字符串不需要加引号
print(y)
print(f"I said: {x}")
print(f"I also said: '{y}'")
hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}"
print(joke_evaluation.format(hilarious))#  .format格式化什么用？
w="this is the left side of..."
e="a string with a right side"
print(w + e)
