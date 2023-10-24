import math 

def userInputValue(text):
    value = int(input(text))
    return value 

def calculating_Value_n_and_Value_m():
    n = userInputValue("Enter your n: ")
    m = userInputValue("Enter your m: ")
    return n, m

n,m=calculating_Value_n_and_Value_m()

def generateMatrix(m, n):
    matrix = [[0] * m for element in range(n)]
    return matrix

def calculatingOfResult(matrix):
    for elementI in range(1,n+1):
        for elementJ in range(m):
            matrix[elementI-1][elementJ-1]=math.log10(1 + abs(elementI - elementJ) + pow(math.e, -math.sqrt(elementI + elementJ)))
    return matrix

def outputResult(matrix, n, m):
    for elementI in range(n):
        for elementJ in range(m):
            print(round(matrix[elementI][elementJ], 3), end="\t")
        print()

def main():
    print(outputResult(calculatingOfResult(generateMatrix(m, n)), n, m))

if __name__ == "__main__":
    main()