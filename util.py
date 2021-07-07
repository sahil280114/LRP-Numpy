import numpy
import matplotlib
from matplotlib import pyplot as plt

#Load Data

def loaddata():
    X = numpy.loadtxt('data/X.txt')
    T = numpy.loadtxt('data/T.txt')
    return X,T

#Load Parameters
def loadparams():
    W = [numpy.loadtxt('params/l%d-W.txt'%l) for l in range(1,4)]
    B = [numpy.loadtxt('params/l%d-B.txt'%l) for l in range(1,4)]
    return W,B

#Visualisation

def heatmap(R,sx,sy):

    b = 10*((numpy.abs(R)**3.0).mean()**(1.0/3))

    from matplotlib.colors import ListedColormap
    my_cmap = plt.cm.seismic(numpy.arange(plt.cm.seismic.N))
    my_cmap[:,0:3] *= 0.85
    my_cmap = ListedColormap(my_cmap)
    plt.figure(figsize=(sx,sy))
    plt.subplots_adjust(left=0,right=1,bottom=0,top=1)
    plt.axis('off')
    plt.imshow(R,cmap=my_cmap,vmin=-b,vmax=b,interpolation='nearest')
    plt.show()

def digit(X,sx,sy):

    plt.figure(figsize=(sx,sy))
    plt.subplots_adjust(left=0,right=1,bottom=0,top=1)
    plt.axis('off')
    plt.imshow(X,interpolation='nearest',cmap='gray')
    plt.show()