#!/usr/bin/python
# -*- coding=utf-8 -*-
#对于面向对象的封装来说，其实就是使用构造方法将内容封装到 对象 中，然后通过对象直接或者self间接获取被封装的内容。
class persion():
    def __init__(self,name,sex,age,fig):
        self.name = name
        self.sex = sex
        self.age = age
        self.fig =fig
    def grass(self):
        self.fig = self.fig - 200
    def incest(self):
        self.fig = self.fig + 100
    def duo(self):
        self.fig = self.fig - 500
    def time(self):
        tem = print("姓名:%s,性别:%s,年龄:%s,战斗力:%s" %(self.name,self.sex,self.age,self.fig))

cang = persion('cang','woman',27,1700)
boduo = persion('bo','woman','29',2400)
ni = persion('per','man',45,2800)
ni.grass()
cang.duo()
boduo.incest()
cang.time()
boduo.time()
ni.time()
ni.grass()
ni.time()