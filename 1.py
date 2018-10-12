#!/usr/bin/python
# -*- coding=utf-8 -*-
class a():
    def __init__(self,name,age):
        self.aa = name
        self.bb = age
    def ss(self):
            print("name is %s,age is %s" %(self.aa,self.bb))
class b(a):
    def ss(self):
        pass


def qw(obj):
    obj.ss()




c = b('12',12)
qw(c)
print(c)