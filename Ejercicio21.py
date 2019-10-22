import numpy as np
import matplotlib.pylab as plt

x = np.linspace(0,np.pi*2,100)
y = np.sin(x)
plt.plot(x,y,c='g')
plt.grid()
plt.show()