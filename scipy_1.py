

'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
x = np.arange(0, 10)
y = np.exp(-x/3.0)
f = interpolate.interp1d(x, y)

xnew = np.arange(0, 9, 0.1)
ynew = f(xnew)   # use interpolation function returned by `interp1d`
plt.title('Exponential interpolation')
#plt.plot(x, y, 'o', xnew, ynew, '-', color='green')
plt.plot(x,y,'o')
plt.plot(xnew, ynew)
plt.legend(['data', 'linear'], loc='best')
plt.show()


from scipy import constants
print("One liter in cubic meters:", constants.liter)

import numpy as np
from scipy.interpolate import interp1d
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 3, 5, 8])
f = interp1d(x, y)
print("Interpolated value at x=2.5:", f(2.5))

from scipy.integrate import quad
def integrand(x):
    return x**2
result, _ = quad(integrand, 0, 2)
print("Integral of x^2 from 0 to 2:", result)

import numpy as np
from scipy.linalg import solve
A = np.array([[2, 1], [1, 3]])
b = np.array([5, 8])
x = solve(A, b)
print("Solution x:", x)

import numpy as np
from scipy.optimize import curve_fit
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c
x_data = np.array([0, 1, 2, 3, 4])
y_data = np.array([1, 3, 6, 10, 15])
params, _ = curve_fit(quadratic, x_data, y_data)
print("Fitted parameters (a, b, c):", params)

import numpy as np
from scipy.optimize import fsolve

# Define your quadratic function
def quadratic_equation(x, a, b, c):
    return a * x**2 + b * x + c

# Coefficients of the quadratic equation: ax^2 + bx + c = 0
a = 0.5
b = 1.5
c = 1.0

roots = fsolve(quadratic_equation, [1, 1], args=(a, b, c))
print("Roots of the quadratic equation:", roots)

from scipy.optimize import fsolve
import math

def equations(p):
    x, y = p
    eq1 = x + y**2 - 4
    eq2 = math.exp(x) + x * y - 3
    return [eq1, eq2]

x, y = fsolve(equations, (1, 1))
print("Solutions (x, y):", x, y)

import numpy as np
from scipy.optimize import minimize

# Define the function to be minimized
def objective(x):
    return x**2 + 2*x + 1

# Perform the minimization
result = minimize(objective, x0=0)
print("Optimal value:", result.x)
print("Function value at optimal point:", result.fun)

import numpy as np
from scipy.linalg import solve

# Coefficient matrix
A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])

# Right-hand side vector
b = np.array([1, -2, 0])

# Solve the system
x = solve(A, b)
print("Solution of the system:", x)

from scipy.integrate import quad

# Define the function to be integrated
def integrand(x):
    return np.exp(-x**2)

# Perform the integration
result, error = quad(integrand, 0, np.inf)
print("Integral result:", result)
print("Estimated error:", error)

import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Sample data points
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Create an interpolation function
f = interp1d(x, y, kind='cubic')

# Interpolated values
x_new = np.linspace(0, 10, 100)
y_new = f(x_new)

# Plotting the results
plt.plot(x, y, 'o', label='data points')
plt.plot(x_new, y_new, '-', label='cubic interpolation')
plt.legend()
plt.show()

'''

'''
import numpy as np
from scipy.fft import fft, ifft
import matplotlib.pyplot as plt

# Sample signal
t = np.linspace(0, 1, 400)
x = np.sin(50 * 2 * np.pi * t)

# Perform FFT
X = fft(x)
print(X[3:8])

# Inverse FFT
x_reconstructed = ifft(X)

# Plotting the results
plt.figure()
plt.subplot(4, 1, 1)
plt.plot(t, x)
plt.title('Original Signal')

plt.subplot(4, 1, 2)
plt.plot(t, np.abs(X))
plt.title('FFT(Amplitude) of the Signal')

plt.subplot(4, 1, 3)
plt.plot(t, np.angle(X))
plt.title('FFT(Phase) of the Signal')

plt.subplot(4, 1, 4)
plt.plot(t, x_reconstructed.real)
plt.title('Reconstructed Signal from IFFT')

plt.tight_layout()
plt.show()

import numpy as np
from scipy import stats

# Sample data
data = np.array([1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10])

# Calculate descriptive statistics
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)
std_dev = np.std(data)
variance = np.var(data)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode.mode[0], "with count:", mode.count[0])
print("Standard Deviation:", std_dev)
print("Variance:", variance)

from scipy.stats import norm

# Generate 10 samples from a normal distribution with mean 5 and standard deviation 2
samples = norm.rvs(loc=5, scale=2, size=10)
print(samples)

'''

'''
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Generate a signal
fs = 1000  # Sample frequency
t = np.linspace(0, 1, fs, False)  # Time array
x = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# Filter the signal
b, a = signal.butter(5, 0.1, 'low')
y = signal.lfilter(b, a, x)


# Plot the signals
plt.plot(t, x, label='Original signal')
plt.plot(t, y, label='Filtered signal')
plt.legend()
plt.show()

'''

'''
from scipy import linalg
import numpy as np

# Define a matrix
A = np.array([[1, 2], [3, 4]])

# Compute the eigenvalues and eigenvectors
w, v = linalg.eig(A)

# Print the eigenvalues and eigenvectors
print('Eigenvalues:', w)
print('Eigenvectors:', v)


from scipy.optimize import minimize_scalar

# Function to minimize
def f(x):
    return x**2 + 10*np.sin(x)

# Minimize the function
res = minimize_scalar(f)
print(res.x)  # Output is the x-value that minimizes the function
'''

import numpy as np
from scipy.io import savemat, loadmat

# Create a sample array
array = np.ones((4, 4))

# Save to a .mat file
savemat('example.mat', {'ar': array})

# Load data from the .mat file
data = loadmat('example.mat')
loaded_array = data['ar']

print(loaded_array)  # Should print the original array