
import matplotlib.pyplot as plt
import numpy as np
import time as time
import os

timestr = str(time.time())
os.mkdir("4-visualizing_matrices\\" + timestr)
steps = 40

###############################################################################
# A is the 2x2 transition array, and x is the initial voter distribution %.
###############################################################################
A = np.array([[0.96, 0.02],[0.04, 0.98]])
x = np.array([50,50])


###############################################################################
# We want to plot the bar charts, then re-evaluate x. We repeat this procedure
# steps number of times.
###############################################################################
for i in range(steps):
    plt.clf() #So the bars don't overlap.
    plt.bar(['Democrat', 'Republican'],x)
    plt.ylim([0,70])
    plt.title("Distribution of Republicans and Democrats in a County")
    plt.ylabel("Percentage of Population")
    plt.savefig("4-visualizing_matrices\\" + timestr + "\\"+ str(i) + ".png", dpi = 300)

    x = np.matmul(A,x)

#Show the plot.
plt.show()
