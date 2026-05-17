from prime_check import check_prime

if __name__ == '__main__':
    x = int(input("enter a number :  "))
    try:
        print(check_prime(x))
    except ValueError:
        print("enter a positive integer")
    finally:
        input("\nPress Enter to close...")

