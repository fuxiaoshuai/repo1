#!/usr/bin/python
# -*- coding=utf-8 -*-
import os
import shutil
def dir():
    input_path = input("输入你想创建的目录:")
    if not os.path.exists(input_path):
        print("文件夹或者文件不存在%s" %(input_path))
        print('*' * 30)
        os.makedirs(input_path)
        if os.path.exists(input_path):
            print("创建成功%s" %(input_path))
    elif not os.listdir(input_path):
        print("文件夹为空%s" %(input_path))

def file():
    input_path1 = input("输入你想创建的文件:")
    if not os.path.exists(input_path1):
        print("文件夹或者文件不存在%s" % (input_path1))
        print('*' * 30)
        os.mknod(input_path1)
        if os.path.exists(input_path1):
            print("创建成功%s" % (input_path1))
        elif not os.listdir(input_path1):
            print("文件夹为空%s" % (input_path1))


while True:
    xuan = input("请选择你想创建目录还是文件。1:目录，2:文件！")
    if xuan == '1':
        dir()
        break
    elif xuan == '2':
        file()
        break
    else:
        print("调皮，正确输入！")
        xuan = input("请选择你想创建目录还是文件。1:目录，2:文件！")









