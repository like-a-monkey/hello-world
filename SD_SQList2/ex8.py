formatter="{} {} {} {}"


#substitude='1 2 3 4'
#print(f"{substitude}") how to make the equal thing with differert way
#print(f"{formatter}")


print(formatter.format(1,2,3,4))#error 是逗号不是空格          
print(formatter.format("one","two","three","four"))
# ｛｝花括号与四项匹配起来，简单的代入
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))
