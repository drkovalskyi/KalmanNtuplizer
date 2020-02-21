#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
import VF
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 15:19:20 2015

@author: gflouris
"""
class FileOps:
    def write_file(self, name, comments):
        global file
        file = open(name,"w")
        file.write(comments)
        file.write("..\n")

    def write_line(self, p1, p2, p3, p4, p5, p6, p7):
        file.write("   "+str(p1)+"\t"+str(p2)+"\t"+str(p3)+"\t"+str(p4)+"\t"+str(p5)+"\t"+str(p6)+"\t"+str(p7)+"\n")
