import math

def f(x):
    # Define the function to integrate here
    return math.sin(x)

def trapezoidal_rule(a, b, n):
    # Calculate the trapezoidal rule approximation of the definite integral
    h = (b-a)/n
    s = 0.5*(f(a) + f(b))
    for i in range(1, n):
        s += f(a + i*h)
    return h*s

# Test the program on two different functions
result1 = trapezoidal_rule(0, math.pi/2, 1000)
result2 = trapezoidal_rule(0, 1, 1000)

print("Result for sin(x) from 0 to pi/2:", result1)
print("Result for x^2 from 0 to 1:", result2)
