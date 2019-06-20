import matplotlib.pyplot as plt
import numpy as np
import time as time
import os

timestr = str(time.time())
os.mkdir("4-visualizing_matrices\\" + timestr)
steps = 20

###############################################################################
# A is the 4x4 transition array, and x is the initial voter distribution %.
###############################################################################
A = np.array([[0.85,0.05, 0.1,0.4],[0.05,0.9,0.05,0.05],[0.05,0.03,0.75,0.05],[0.05,0.02,0.1,0.5]])
x = np.array([25,25,25,25])

###############################################################################
# We want to plot the bar charts, then re-evaluate x. We repeat this procedure
# steps number of times.
###############################################################################
for i in range(steps):
    plt.clf() #So the bars don't overlap.
    plt.bar(['MORENA','PAN', 'PRI', "Independent"],x)
    plt.title("Distribution of Political Affiliations")
    plt.ylabel("Percentage of State Population")
    plt.ylim([0,100])
    plt.savefig("4-visualizing_matrices\\" + timestr + "\\"+ str(i) + ".png", dpi = 300)

    x = np.matmul(A,x)


plt.show()
