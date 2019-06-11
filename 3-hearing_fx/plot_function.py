import matplotlib.pyplot as plt
import numpy as np



xs = np.linspace(0,10,1000)
ys = np.sin(xs * xs)

for i in range(100): #enumerate(zip(xs,ys)):

    plt.clf()
    plt.scatter(i/10,np.sin((i/10)**2))
    plt.plot(xs,ys)
    plt.axis([-1,11,-6,10])
    plt.grid()
    plt.savefig(str(i)+".png")
