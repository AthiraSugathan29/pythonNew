try:
    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter second number : "))
    n3 = n1/n2
    print(n3)
except Exception as er:
    print(er)
# except ZeroDivisionError as er:
#     print(er)
# except ValueError as er:
#     print(er)