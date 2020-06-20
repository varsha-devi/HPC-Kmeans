import numpy as np
import matplotlib.pyplot as plt


ref_par2=np.array([[0,0.01,0.03],[0,0.02,0.15],[0,0.03,0.05]])
ref_par4=np.array([[0,0.01,0.04],[0,0.04,0.24],[0,0.04,0.06]])
ref_par6=np.array([[0,0,0.05],[0.01,0.04,0.27],[0,0.05,0.07]])
Nvec=[500,5000,50000]
Kvec=[3,4,6]

# cd hpc-kmeans

method='Sequential' # 'OpenMP' or 'Sequential'
N=5000 # number of points
k=3 # number of clusters
thread=2

if method=='OpenMP':
    times=np.loadtxt('{}_time_N{}_K{}_thread{}'.format(method,N,k,thread))
else:
    times=np.loadtxt('{}_time_N{}_K{}'.format(method,N,k))

## Execution time w.r.t. number of points
indK=2
K=Kvec[indK]

time_par2=[]
time_par4=[]
time_par6=[]
time_seq=[]


for N in Nvec:
    thread=2
    method='OpenMP'
    times=np.loadtxt('{}_time_N{}_K{}_{}threads.txt'.format(method,N,K,thread))
    time_par2.append(np.mean(times))
    
    thread=4
    method='OpenMP'
    times=np.loadtxt('{}_time_N{}_K{}_{}threads.txt'.format(method,N,K,thread))
    time_par4.append(np.mean(times))
    
    thread=6
    method='OpenMP'
    times=np.loadtxt('{}_time_N{}_K{}_{}threads.txt'.format(method,N,K,thread))
    time_par6.append(np.mean(times))

    method='Sequential'
    times=np.loadtxt('{}_time_N{}_K{}.txt'.format(method,N,K))
    time_seq.append(np.mean(times))


plt.figure()
plt.semilogx(Nvec,time_seq,'o--',label='sequential')
plt.semilogx(Nvec,time_par2,'o-',label='OpenMP 2 threads')
plt.semilogx(Nvec,time_par4,'o-',label='OpenMP 4 threads')
plt.semilogx(Nvec,time_par6,'o-',label='OpenMP 6 threads')
plt.semilogx(Nvec,ref_par2[indK,:],'x',label='ref 2 threads')
plt.semilogx(Nvec,ref_par4[indK,:],'x',label='ref 4 threads')
plt.semilogx(Nvec,ref_par6[indK,:],'x',label='ref 6 threads')
plt.xlabel('number of points')
plt.ylabel("mean time")
plt.legend()
plt.title("Execution time with {} clusters".format(K))
plt.savefig("Time_vs_nb_points_{}clusters".format(K))
plt.show()


## Execution time w.r.t. number of clusters
indN=2
N=Nvec[indN]

time_par2=[]
time_par4=[]
time_par6=[]
time_seq=[]

for K in Kvec:
    thread=2
    method='OpenMP'
    times=np.loadtxt('{}_time_N{}_K{}_{}threads.txt'.format(method,N,K,thread))
    time_par2.append(np.mean(times))
    
    thread=4
    method='OpenMP'
    times=np.loadtxt('{}_time_N{}_K{}_{}threads.txt'.format(method,N,K,thread))
    time_par4.append(np.mean(times))    

    thread=6
    method='OpenMP'
    times=np.loadtxt('{}_time_N{}_K{}_{}threads.txt'.format(method,N,K,thread))
    time_par6.append(np.mean(times))   
    
    method='Sequential'
    times=np.loadtxt('{}_time_N{}_K{}.txt'.format(method,N,K))
    time_seq.append(np.mean(times))




plt.figure()
plt.plot(Kvec,time_seq,'o-',label='sequential')
plt.plot(Kvec,time_par2,'o-',label='OpenMP 2 threads')
plt.plot(Kvec,time_par4,'o-',label='OpenMP 4 threads')
plt.plot(Kvec,time_par6,'o-',label='OpenMP 6 threads')
plt.plot(Kvec,ref_par2[:,indN],'x',label='ref 2 threads')
plt.plot(Kvec,ref_par4[:,indN],'x',label='ref 4 threads')
plt.plot(Kvec,ref_par6[:,indN],'x',label='ref 6 threads')
plt.xlabel('number of clusters')
plt.ylabel("mean time")
plt.legend()
plt.title("Execution time with {} points".format(N))
plt.savefig("Time_vs_nb_pclusters_{}points".format(N))
plt.show()



## Execution time w.r.t. number of threads
N=5000
K=4

nb_threads=[2,3,4,5,6]
time_par=[]

for thread in nb_threads:
    method='OpenMP'
    times=np.loadtxt('{}_time_N{}_K{}_thread{}.txt'.format(method,N,k,thread))
    time_par.append(np.mean(times))




plt.figure()
plt.plot(nb_threads,time_par,'o-',label='OpenMP')
plt.xlabel('number of threads')
plt.ylabel("mean time")
plt.legend()
plt.title("Execution time")
plt.show()








