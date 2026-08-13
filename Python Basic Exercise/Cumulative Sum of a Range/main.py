print("Printing current and previous number sum in a range(10)")

for i in range(10):
    if i == 0:
        print("Current Number 0 Previous Number 0 Sum: 0")
    else:
        print(f"Current Number {i} Previous Number {i-1} Sum: {(i) + (i-1)}")
