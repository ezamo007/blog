import numpy as np
import matplotlib.pyplot as plt

####################################
#Setup
####################################
max_x = np.pi
min_x = -max_x
scale = 2 * np.pi / (max_x - min_x)
num_points = 300
n = 10
steps = 10000
x = np.linspace(min_x, max_x, num_points)

#####################################
#Thee target function is defined here
#####################################
y_exact = np.sin(np.exp(x))

def evaluate(cos_coeff, sin_coeff, error = False):
    sum = np.zeros(num_points)
    for i , (an, bn) in enumerate(zip(cos_coeff, sin_coeff)):
        sum += an * np.cos(i * x * scale) + bn * np.sin(i * x * scale) #- mid)
    if error:
        return np.sum((sum - y_exact) ** 2)
    return sum

def optimize(cos_coeff, sin_coeff):
    test_cos = list(cos_coeff)
    test_sin = list(sin_coeff)
    index = np.random.randint(n)
    if np.random.random() < 0.5:
        test_cos[index] += np.random.random() - 0.5
    else:
        test_sin[index] += np.random.random() - 0.5
    if evaluate(test_cos, test_sin, error = True) < evaluate(cos_coeff, sin_coeff, error = True):
        return test_cos, test_sin
    else:
        return cos_coeff, sin_coeff


#######################################################
#Where the magic happens.
#The coefficient arrays start at zero and are randomly
#nudged until the steps have been exhausted.
#######################################################
cos_coeff = np.zeros(n)
sin_coeff = np.zeros(n)
y_approx = np.zeros(num_points)

for i in range(steps):
    cos_coeff, sin_coeff = optimize(cos_coeff, sin_coeff)
    y_approx = evaluate(cos_coeff, sin_coeff)

    #####################################################
    #Saves images for producing animation of the process.
    #####################################################
    if i % 10 == 0:
        plt.clf()
        plt.plot(x, y_approx)
        plt.plot(x, y_exact)
        #plt.savefig("2-fourier_coefficients\\images\\"+str(i // 10) + ".png")

print("Cosine Coefficients: ", np.round(cos_coeff,3))
print("Sine Coefficients: ", np.round(sin_coeff,3))



#########################
#Prints out the equations
#########################
cos_string = ""
sin_string = ""
for i in range(n):
    cos_string += str(np.round(cos_coeff[i],3)) + " cos(" + str(i) + "x) + "
    sin_string += str(np.round(sin_coeff[i],3)) + " sin(" + str(i) + "x) + "
equation = "Equation: " + cos_string + sin_string
equation = equation[0:len(equation)-2]
print(equation)

##################################
#Plots equation and approximation.
##################################
plt.show()
