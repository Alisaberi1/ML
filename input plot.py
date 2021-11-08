
import numpy as np
import matplotlib.pyplot as plt
from random import sample

#p=programing,oop=object orinted programing
x=np.linspace(0,5,11)
y=x**2

fig,ax=plt.subplots(1,4,figsize=(12,5),dpi=100)
ax[0].plot(x,x**2,x,x**3 )
a=input("name:")
a1=input("name:")
a2=input("name:")
ax[0].set_title(a)
ax[1].plot(x,x**2,x,x**3)
ax[1].set_title(a1)
ax[2].plot(x,x**2,x,x**3 )
ax[2].set_title(a2)
ax[2].set_ylim([0,5])
ax[2].set_xlim([0.5,0.8])
line,=ax[3].plot(x,x+8,color="black",lw=1)
line.set_dashes([5,10,20,5])
data=sample(range(0,1000), 110)
#k means the len of choise number in range (d,f) 
print(len(data))
# bin means the number of data 
print(plt.hist(data,bins=list(range(0,1000,5))))