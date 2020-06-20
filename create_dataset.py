import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

N=5000 # nb of points
K=4 # nb of clusters
d=3 # dimension EITHER 2 or 3

mu=np.random.randint(-10,10,(3,K))
sigma=np.random.rand(K)+1
points=np.zeros((3,N))


for n in range(N):
    k=np.random.randint(0,K)
    points[:,n]=mu[:,k]+sigma[k]*np.random.rand(3) # d = 3 (even for d = 2)

if d==2:
    points[2,:] = 0 # set third dimension to 0 (d = 2)


if d==2:
    plt.figure()
    plt.plot(points[0,:],points[1,:],'o')
    plt.show()

if d==3:
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(points[0,:],points[1,:],points[2,:])
    plt.show()


file=open("dataset_N{}_K{}_D{}.txt".format(N,K,d),"w")
file.write("{} \n".format(N))
for n in range(N):
    for i in range(3): # even for d = 2
        file.write("{} ".format(points[i,n]))
    file.write("\n")
file.close()


