
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

num = int(input("Enter a number :"))
factorial = factorial(num)
print("The factorial of ", num, " is : ", factorial)

# Output:
# Enter a number : 5
# The factorial of  5  is :  120
