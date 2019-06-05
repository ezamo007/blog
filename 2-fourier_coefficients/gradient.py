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
y_exact = np.sin(np.exp(x))#np.exp(-x*x)


def F_cos(cos_coeff):
    sum = np.zeros(num_points)
    for i , an in enumerate(cos_coeff):
        sum += an * np.cos(i * x * scale) #+ bn * np.sin(i * x * scale) #- mid)
    return np.sum((sum - y_exact) ** 2)

def F_sin(sin_coeff):
    sum = np.zeros(num_points)
    for i , an in enumerate(sin_coeff):
        sum += an * np.sin(i * x * scale) #+ bn * np.sin(i * x * scale) #- mid)
    return np.sum((sum - y_exact) ** 2)


def gradF_cos(cos_coeff):
    grad = np.zeros(n)
    for i in range(n):
        test_cos_coeff = list(cos_coeff)
        test_cos_coeff[i] += 0.001
        grad[i] = - F_cos(test_cos_coeff) + F_cos(cos_coeff)
    grad = grad / np.linalg.norm(grad)
    return grad

def gradF_sin(sin_coeff):
    grad = np.zeros(n)
    for i in range(n):
        test_sin_coeff = list(sin_coeff)
        test_sin_coeff[i] += 0.001
        grad[i] = - F_sin(test_sin_coeff) + F_sin(sin_coeff)
    grad = grad / np.linalg.norm(grad)
    return grad



#######################################################
#Where the magic happens.
#The coefficient arrays start at zero and are randomly
#nudged until the steps have been exhausted.
#######################################################
cos_coeff = np.zeros(n)
sin_coeff = np.zeros(n)

delta = 1
for i in range(steps):
    cos_coeff += delta * gradF_cos(cos_coeff)
    sin_coeff += delta * gradF_sin(sin_coeff)
    delta = 1 - i / steps

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

#######################################
#Evaluates and plots the approximation.
#######################################
sum = np.zeros(num_points)
for i , (an, bn) in enumerate(zip(cos_coeff, sin_coeff)):
    sum += an * np.cos(i * x * scale) + bn * np.sin(i * x * scale)
plt.plot(x,sum)
plt.plot(x, y_exact)
plt.show()
