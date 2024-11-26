name = input("Enter Your good name:")
num1 = int(input("Enter your favorite number:"))
num2 = int(input("Enter your favorite number:"))
num3 = int(input("Enter your favorite number:"))
fav_number = [num1,num2,num3]
print(f"Hi {name} lets come and explore your numbers")
if num1 % 2 == 0:
    print(f"The number {num1} is even")
else:
    print(f"The number {num1} is odd")
if num2 % 2 == 0:
    print(f"The number {num2} is even")
else:
    print(f"The number {num2} is odd")
if num3 % 2 == 0:
    print(f"The number {num3} is even")
else:
    print(f"The number {num3} is odd")
print("The square of your favorite numbers is:")
print(f"The number {num1} and its square is: ({num1},{num1**2})")
print(f"The number {num2} and its square is: ({num2},{num2**2})")
print(f"The number {num3} and its square is: ({num3},{num3**2})")
total_sum =sum(fav_number) 
print(f"The sum of your favorite numbers is {total_sum}")
def is_prime(num):
    if num < 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False   
    return True

if is_prime(total_sum):
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number.")