def userInputFloatValue(text):
    return float(input(text))

def calculateF(a, b, c, d):
    return pow((a + b + c + d), 2)

def calculateG(a, b, c, d):
    return (pow(a, 3) + pow(b, 3) + pow(c, 3) + pow(d, 3))

def calculateSum(f, g):
    return f + g

def main():
    a, b, c, d = userInputFloatValue("Enter a: "), userInputFloatValue("Enter b: "), userInputFloatValue("Enter c: "), userInputFloatValue("Enter d: ")
    F = calculateF(a, b, c, d)
    G = calculateG(a, b, c, d)
    print(f"F = {F}, G = {G}, and their sum is - {calculateSum(F, G)}")

if __name__ == "__main__":
    main()