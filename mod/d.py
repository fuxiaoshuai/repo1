#!/usr/bin/python
# -*- coding=utf-8 -*-
i=0
j=0
while i<9:
    i+=1
    while j<9:
        j+=1
        print(j,"x",i,"=",i*j,"\t",end="")
        if i==j:
            j=0
            print("")
            break
