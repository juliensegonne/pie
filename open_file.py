import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


file=open("test.txt","r")
r=file.read()
table = [float(num) for num in r.split()]
#print(table)

T=[]
time=[]



for i in range(len(table)) :
    if i%2==0 :
        T.append(table[i])
    else :
        time.append(table[i])

#print(time,T)

plt.plot(time,T)
plt.show()

file.close()

