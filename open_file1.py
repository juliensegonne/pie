import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

file=open("test1.txt","r")
r=file.read()
table = [data for data in r.split()]
#print(table)

T=[]
time=[]



for i in range(len(table)) :
    if i%2!=0 :
        T.append(float(table[i]))
    else :
        time.append(datetime.strptime(table[i], '%Y-%m-%d;%H:%M:%S'))

#print(time,T)

plt.plot(time,T)
plt.show()

file.close()

