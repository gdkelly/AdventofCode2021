# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 13:09:28 2021

@author: Greg.Kelly
"""
import numpy as np
import pandas as pd

df=pd.read_csv('input_day_5.txt',header=None,sep=",")
df[['y1','x2']]=df[1].str.split("->",expand=True)
df['x2']=df['x2'].str.split(expand=True)
df['y1']=df['y1'].str.split(expand=True)

vents=np.zeros([1000,1000])

for i in range(0,len(df)):
    x1=int(df.loc[i,0])
    y1=int(df.loc[i,'y1'])
    x2=int(df.loc[i,'x2'])
    y2=int(df.loc[i,2])
    
    if x1 == x2:
        x=x1
        y_range=abs(y2-y1)
        if y2 > y1:
            y_high=y2
            y_low=y1
        if y1 > y2:
            y_high=y1
            y_low=y2
            
        for v in range(y_low,y_high + 1):
            vents[v,x]+=1
            
    if y1 == y2:
        y=y1
        x_range=abs(x2-x1)
        if x2 > x1:
            x_high=x2
            x_low=x1
        if x1 > x2:
            x_high=x1
            x_low=x2
            
        for v in range(x_low,x_high + 1):
            vents[y,v]+=1
            
    if abs(x1-x2) == abs(y1-y2):
        steps=abs(x1-x2)
        if x2 > x1  and y2>y1:
            for u in range(0,steps+1):
                vents[y1+u,x1+u]+=1
        if x2 > x1 and y1>y2:
            for u in range(0,steps+1):
                vents[y1-u,x1+u,]+=1
        if x1 > x2 and y1>y2:
            for u in range(0,steps+1):
                vents[y1-u,x1-u,]+=1
        if x1 > x2 and y2>y1:
            for u in range(0,steps+1):
                vents[y1+u,x1-u]+=1


            
            
            

count=np.where(vents>=2)    
overlaps=len(count[0])    
print(overlaps)