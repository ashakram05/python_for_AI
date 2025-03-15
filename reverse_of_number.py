num = int(input("Enter a number :"))
reminder = 0

while(num > 0):
    digit = num % 10
    reminder = reminder * 10 + digit
    num = num // 10     

print("The reverse number is : ", reminder)

# Output: Enter a number : 123
#         The
#         reverse number is : 321

# Output: Enter a number : 123456
#         The
#         reverse number is : 654321

