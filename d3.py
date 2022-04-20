
"""
Created on Wed Apr 20 12:17:23 2022

@author: piotr
"""

from keybert import KeyBERT
import pandas as pd
from sys import exit    
data_frame2 = pd.read_csv('def1.csv', sep='\|',encoding = "ISO-8859-1", error_bad_lines=False)  
for col in data_frame2.columns:
    print(col)
#data_frame2 
descr=data_frame2.iloc[:,[5,8]]
descrt=data_frame2.iloc[:,[5]]
descrd=data_frame2.iloc[:,[8]]
descr_l = descr.values.tolist()
print(descrt.columns.tolist())
df2=descrt['"EVENTTIMESTAMP"'].str.split(',',expand=True,)
print(df2.columns.tolist())
df3=df2[0]
from datetime import datetime
#ss=datetime.fromisoformat('22/01/05  12:48:16').timestamp()
1394004146.976637
ss1='22/01/05  12:48:16'

import datetime
date = '2021-05-21 11:22:03'
ss1='22/01/05  12:48:16'
datem = datetime.datetime.strptime(ss1, "%y/%m/%d %H:%M:%S")
print(datem.day)        # 25
print(datem.month)      # 5
print(datem.year)       # 2021
print(datem.hour)       # 11
print(datem.minute)     # 22
print(datem.second)     # 3
time1=datem.second +60*datem.minute+3600*datem.hour+3600*24*datem.day

def seconds1(ss1):
    datem = datetime.datetime.strptime(ss1, "%y/%m/%d %H:%M:%S")
    time1=datem.second +60*datem.minute+3600*datem.hour+3600*24*datem.day+datem.month*30*3600*24
    return time1
df4=df3
df5=df4.apply(seconds1)

#frames = [df5, descrd]
zz=pd.concat((df5,descrd), axis=1)
#result = pd.concat(frames)
zz1=zz.sort_values(by=[0])
#print(result)