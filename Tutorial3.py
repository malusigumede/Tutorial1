from numpy.fft import fft,ifft
import numpy as np
import matplotlib.pyplot as plt

#Question1
def conv(x,y):
    ft1=fft(x)
    ft2=fft(y)

def myshift(x,n=0):
    N=x.size
    vec=np.zeros(N) 
    vec[n]=1
    vecft=fft(vec)
    ft1=fft(x)
    return np.real(ifft(ft1*vecft))
    
if __name__=='__main__':
    x=np.arange(-10,10,0.1)
    y=np.exp(-0.5*(x+5)**2/1.5**2)
    M=y.size
    yshift=myshift(y,M/2)
    plt.plot(x,y)
    plt.plot(x,yshift)
    plt.show() 
    
    #Question2
    
