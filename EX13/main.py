import math

def volMassEllipsoide(a=1, b=1, c=1, density=1):
    volume = (4 / 3) * math.pi * a * b * c
    mass = volume * density
    return volume, mass


print(volMassEllipsoide())

print(volMassEllipsoide(2, 3, 4, 2))

print(volMassEllipsoide(a=2, c=3, density=1))