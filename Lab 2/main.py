import math

def f(x):
    return float(4 * x * math.cos(x))/(math.pi*(pow(x, 2) - 1))


with open("параметри.txt", "r") as pfile:
    a, b, delta_x = map(float, pfile.readline().split())

with open("результати.txt", "w") as result_file:
    x = a
    while x <= b:
        result = f(x)
        result_file.write(f"x = {x}, f(x) = {result}\n")
        x += delta_x

