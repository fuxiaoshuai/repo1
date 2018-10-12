#!/usr/bin/python
# -*- coding=utf-8 -*-
class aninos():
    def chi(self):
        print("吃喝拉撒")

class dog(aninos):
    def jiao(self):
        print("汪汪汪")

class cat(aninos):
    def jiao(self):
        print("喵喵喵")

def ac(obj):
    obj.jiao()
    obj.chi()


b = cat()
b.chi()
b.jiao()

c = dog()
ac(c)

