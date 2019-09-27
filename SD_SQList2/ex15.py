from sys import argv
script,filename = argv

txt = open(filename)#打开文件，并将文件返回给txt,注意此时txt为文件,即file

print(f"Here's your file {filename}:")
#print(txt.read())#txt执行read命令
txt.read()
print("Type the filename again:")

file_again=input("> ")

txt_again = open(file_again)

print(txt_again.read())


#filename = input()
#txt=open(filename)
#print(txt.read())
