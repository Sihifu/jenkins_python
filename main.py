import numpy as np
from matplotlib import pyplot as plt
import sklearn

if __name__=="__main__":
    x=np.linspace(0,1,50)
    y=x**2
    plt.plot(x,y)
    plt.show()
