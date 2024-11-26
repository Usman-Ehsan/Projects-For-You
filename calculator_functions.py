def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    if y ==0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y
def modulus(x,y):
    return x % y
def get_numbers():
   num1 = float(input("Enter the first number: "))
   num2 = float(input("Enter the second number: "))
   return num1, num2
def get_operation():
   print("Choose an operation")
   print("1. Addition")
   print("2. Subtraction")
   print("3. Multiplication")
   print("4. Division")
   print("5. Modulus")
   choice = int(input("Enter your choice (1-5): "))
   return choice
def main():
    while True:
        choice = get_operation()
        num1,num2 = get_numbers()
        if choice == 1:
            result = addition(num1,num2)
            print(f"{num1:.0f} + {num2:.0f} = {result:.0f}")
        elif choice == 2:
            result = subtraction(num1,num2)
            print(f"{num1:.0f} - {num2:.0f} = {result:.0f}")
        elif choice == 3:
            result = multiplication(num1,num2)
            print(f"{num1:.0f} * {num2:.0f} = {result:.0f}")
        elif choice == 4:
             try:
                result = division(num1, num2)
                print(f"{num1:.0f} / {num2:.0f} = {result:.0f}")
             except ZeroDivisionError as e:
                print(e)

        elif choice == 5:
            result = modulus(num1,num2)
            print(f"{num1:.0f} % {num2:.0f} = {result:.0f}")

        else:
            print("Invalid choice: Please enter a valid choice")
        count = input("Do you want to continue the calculation. (yes/no):")
        if count.lower() != "yes":
            break
main()