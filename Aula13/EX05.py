from math import pi


def volume(r):
    return (4*pi*r**3)/3


r = int(input("Digite o raio: "))
print(volume(r))
