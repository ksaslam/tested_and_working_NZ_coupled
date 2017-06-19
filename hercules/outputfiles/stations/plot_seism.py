import numpy as np
import matplotlib.pyplot as plt

data= np.loadtxt('station.0')
plt.plot(data[:,0], data[:,9],'b')


#data1=np.loadtxt('station.0_no')
#plt.plot(data1[:,0], data1[:,9], 'r')


plt.show()

