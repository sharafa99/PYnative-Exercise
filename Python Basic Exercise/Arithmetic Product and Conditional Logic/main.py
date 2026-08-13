val1 = int(input("What is the first number: "))
val2 = int(input("What is the second number: "))
def calc(num1, num2):
    if num1 * num2 <= 1000:
        return (num1 * num2)
    else:
        return (num1 + num2)

print(calc(val1, val2))