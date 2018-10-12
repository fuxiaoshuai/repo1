#!/usr/bin/python
# -*- coding=utf-8 -*-
class woman():
    def __init__(self,name):
        self.name = name
        self.age = 18
    def ser(self):
        print("我的年龄是：%s" %self.__age)


xiao = woman("小新")
print(xiao.age)
