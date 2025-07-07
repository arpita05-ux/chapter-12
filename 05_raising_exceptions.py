a = int(input("enter a number:"))
b = int(input("enter second number:"))


if (b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide number by zero")

else:
    print(f"The division a/b is {a/b}")