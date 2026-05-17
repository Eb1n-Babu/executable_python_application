def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

if __name__ == '__main__':
    x = int(input("enter the number"))
    try:
        print(factorial(x))
    except TypeError:
        print("enter a number")
    except ValueError:
        print("enter a number")
    finally:
        input("\nPress Enter to close")