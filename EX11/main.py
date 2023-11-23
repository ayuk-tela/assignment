import math
def cube(x):
    return x ** 3
def volumeSphere(r):
    return (4/3) * math.pi * cube(r)

r = 5
volume = volumeSphere(r)
print('the volume with radius', r, 'is', volume)