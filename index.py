def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = factorial(num)
        print(f"The factorial of {num} is {result}.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
