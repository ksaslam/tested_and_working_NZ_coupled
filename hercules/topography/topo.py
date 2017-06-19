import numpy as np
import matplotlib.pyplot as plt 
vector= np.zeros((40))

#vector[0:10]= np.linspace(2.0, 3.0, num=10)
test=np.linspace(2, 20, 20)
test2=np.linspace(20, 2, 20)
vector[0:20]= test
vector[20:40]= test2
topography= np.zeros((100,100))
#print(vector)
for ii in range(100):
	for jj in range(100):
		if jj>=0 and jj<40:	
			topography[ii,jj]= 1.0
		if jj>=40 and jj<60:
			print(jj, jj-20)
		
			topography[ii,jj]= vector[jj-40]
		if jj>=60:
			topography[ii,jj]= 1.0


plt.plot(topography[1,:])	
plt.show()


f = open('topography.in','w')
for i in range(100):
	for j in range(100):
		f.write("{:E} \n".format(topography[i,j]))