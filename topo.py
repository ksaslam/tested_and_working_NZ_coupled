import numpy as np
import matplotlib.pyplot as plt 
vector= np.zeros((100))

#vector[0:10]= np.linspace(2.0, 3.0, num=10)
test=np.linspace(10, 1000, 50)
test2=np.linspace(1000, 10, 50)
vector[0:50]= test
vector[50:100]= test2
topography= np.zeros((400,400))
#print(vector)
for ii in range(400):
	summ=0
	for jj in range(400):
		if jj>=0 and jj<200:	
			
			topography[ii,jj]= 10.0
		
		if jj>=200 and jj<300:
			topography[ii,jj]= vector[summ]
			summ=summ+1
		if jj>=300:
			topography[ii,jj]= 10.0


plt.plot(topography[1,:])	
plt.show()


f = open('topography.in','w')
for i in range(400):
	for j in range(400):
		f.write("{:E} \n".format(topography[i,j]))