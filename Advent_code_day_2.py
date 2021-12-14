# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:34:59 2021

@author: Greg.Kelly
"""
import pandas as pd


directions=pd.read_csv(r"C:\Users\greg.kelly\advent_code_day_2.txt",header=None)
directions=directions[0].str.split(' ',expand=True)

directions[1]=pd.to_numeric(directions[1])
a=directions.groupby([0]).sum()
depth=a.loc['down']-a.loc['up']
horizontal=a.loc['forward']
print(depth*horizontal)

aim=0
depth=0
hor=0
for index,row in directions.iterrows():
    if row[0] == 'down':
        aim = aim + row[1]
    elif row[0] == 'up':
        aim = aim - row[1]
    elif row[0] == 'forward':
        hor = hor + row[1]
        depth = depth + aim*row[1]


answer = depth * hor
print(answer)
            