n = input("type a number")

try:
    n = int(n)
    result = 1 / n
except ZeroDivisionError:
    print("you cannot divide by zero")
except ValueError:
    print("you cannot divide a number by a string")
except Exception as err:
    print(f"error: {err}")
else:
    print(f"the result of division is {result}")
finally:
    print("My name is carlos Oliveira")
