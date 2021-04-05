def division(num1, num2):
    return num1/num2
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    soln = division(num1, num2)
    print(soln)
except ZeroDivisionError as zerr:
    print(f"Error: {zerr}")
except ValueError as verr:
    print(f"Error: {verr}")
except TypeError as terr:
    print(f"Error: {terr}")
except:
    print("Error occured")
else:
    print("Completed without errors")
finally:
    print("END")


