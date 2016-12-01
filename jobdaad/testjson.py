#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:getFileLastLine.py
User:               Guodong
Create Date:        2016/9/1
Create Time:        11:05
 """

import json
# data = {
#     'name' : 'ACME',
#     'shares' : 100,
#     'price' : 542.23
# }
# with open('data.json', 'w') as f:
#     json.dump(data, f)

# Reading data back
# import linecache
#
#
# # def processJson(inputJsonFile, outputJsonFile):
# with open('1.html', 'r') as fin:
#     # firstline = fin.readlines()
#     # lastline = fin.readlines()
#     count = linecache.getline('1.html', 1)
#     count = count.split('var offers = TAFFY(')
#     # print firstline
#     print count
#     # fout = open(outputJsonFile, 'w')
#
# with open('data.json', 'w') as fout:
#      json.dump(count, fout)

with open('data.json', 'r') as f:
    # data = f.readlines()
    data = json.load(f)
for each in data:
    print each['code']
    print ''

f.close()
# fin.close()
# fout.close()
