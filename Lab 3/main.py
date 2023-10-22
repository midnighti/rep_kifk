import random 
import math 

def listX():
    x = []
    for element in range(13):   x.append(random.randrange(100))
    return x

x = listX()
print(x)

def sort(arr):  
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

print(sort(x))

def operation(arr):
    return (4 * arr[1] * math.cos(arr[12])) / (math.pi * (pow(arr[5], 2) - 1)) 

def main():
    print(operation(sort(x)))

if __name__ == "__main__":
    main()
