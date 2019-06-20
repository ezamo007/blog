
import matplotlib.pyplot as plt
import numpy as np
import time as time
import os

timestr = str(time.time())
os.mkdir("4-visualizing_matrices\\" + timestr)
steps = 40

###############################################################################
# A is the 2x2 matrix, and x is the initial vector.
###############################################################################
A = np.array([[.0, -1],[1, 0]])
x = np.array([5,-5])

###############################################################################
# Fill in the history array to enable the trailing arrows.
###############################################################################
history = []
for i in range(steps):
     x = np.matmul(A,x)
     history += [x]



###############################################################################
# We want to plot the last 'length' number of arrows, and repeat this process
# steps numbers of times.
###############################################################################

for i in range(len(history)):
    length = min(i, 5)
    plt.clf()
    plt.grid()
    plt.axis([-30,30,-30,30])
    for j,x in enumerate(history[i-length:i] ,1):
        ###############################################################################
        #plt.title("Distribution of Republicans and Democrats in a County")
        #plt.ylabel("Percent Republicans")
        #plt.xlabel("Percent Democrats")
        ###############################################################################
        plt.arrow(0,0,x[0], x[1], fc="k", ec="k", alpha = 0.2 * j , head_width=1, head_length=1)
        plt.savefig("4-visualizing_matrices\\" + timestr + "\\"+ str(i) + ".png", dpi = 300)


plt.show()
