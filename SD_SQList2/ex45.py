class student(object):
    pass

s = student()
s1 = student()
def set_age(self, age):
     # 定义一个函数作为实例方法
    self.age = age
def set_score(self, score):

    self.score = score

student.set_score = set_score
from types import MethodType

s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
s1.set_score(60)
print(s.age)
print(s1.score) # 测试结果
