# Simple Message
message = "Hello, this is a message."
print(message)
print("\n")

# Simple Message
print("First message:")
message = "Hello, this is the first message."
print(message)

#message = "Hello, this is the second message."
print("\nSecond message:")
print(message)
print('\n')

# Personal Message
name = "Usman"
print(f"Hello {name}, would you like to learn some Python today?")
print("\n")

# Name Cases
name = "usman sulehri"
print("Lowercase:", name.lower())
print("Uppercase:", name.upper())
print("Title case:", name.title())
print("\n")

# Famous Quote 
print('Andrew Tate once said, “Success is not given its taken”')
print("\n")

# Famous Quote 2
famous_person = "Andrew Tate"
quote = "“Success is not given its taken”"
message = f'{famous_person} once said, {quote}'
print(message)
print("\n")

# Stripping Names
name = "\t\nUsman Sulehri\n\t"
print("Original name:")
print(name)
print("Name with lstrip():")
print(name.lstrip())
print("Name with rstrip():")
print(name.rstrip())
print("Name with strip():")
print(name.strip())
print("\n")

# Variable Sum
x = 5
y = 10
z = 15
sum = x + y + z
print("The sum of x, y, and z is:", sum)
print("\n")

# Variable Swap.
a = 5
b = 10
print("Before the swap:")
print("a =", a)
print("b =", b)
a, b = b, a
print("After the swap:")
print("a =", a)
print("b =", b)
print("\n")

# Favorite Color
favorite_color = "yellow"
print("My favorite color is:", favorite_color)
color_i_love = favorite_color
print("My favorite color is still:", color_i_love)
print("\n")

# Changing Pet Name
pet_name = "Buddy"
pet_name = "Max"
print(pet_name)
print("\n")

# Observing Name Error
#sunshine = "Sunshine"
#print(sunshine)
#print(sunsine)
#print("\n")

#Reassigning Score
score = 100
print("Initial score:", score)
score = 200
print("New score:", score)
print("\n")

#City Name
city = "New York"
print("My favorite city is:", city)
print("\n")

#Title Case Text
text = "python programming"
print(text.title())
print("\n")

#Lowercase Conversion
mixed_string = "PyThOn PrOgRaMmInG"
print(mixed_string.lower())
print("\n")

#Uppercase Conversion
mixed_string = "PyThOn PrOgRaMmInG"
print(mixed_string.upper())
print("\n")

#Current Temperature
temperature = 25
print(f"The current temperature is {temperature} degrees.")
print("\n")

#Printing a Poem
poem = """Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky"""
print(poem)
print("\n")

#Basic Calculator
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1-4): "))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if choice == 1:
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif choice == 2:
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif choice == 3:
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid choice. Please try again.")