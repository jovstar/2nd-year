# Name: Laniwan, Jovit A.
# Subject: Data Structure and Algorithm
# Lab Activity: Python review 
# Deadline: September 22, 2024 11:59pm


# Exercise 1: Temperature converter
print("1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius")

conversion = input("What conversion type to do (Pick 1 or 2): ")
if conversion == '1':
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit:.2f} degrees")
elif conversion == '2':
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"Temperature in Celsius: {celsius:.2f} degrees")
else:
    print("Invalid input. Please enter 1 or 2.")


# Exercise 2: Ohm’s Law Calculator
print("Choose what to calculate: \n1. Voltage \n2. Current \n3. Resistance")
choice = input("Pick a number (1, 2, or 3): ")
try:
    if choice == '1':
        print("\nSolving for VOLTAGE")
        current = float(input("Enter the current in Amperes: "))
        resistance = float(input("Enter the resistance in Ohms: "))
        voltage = current * resistance
        print(f"Voltage: {voltage:.2f} V")
    elif choice == '2':
        print("\nSolving for CURRENT")
        voltage = float(input("Enter the voltage in Volts: "))
        resistance = float(input("Enter the resistance in Ohms: "))
        current = voltage / resistance
        print(f"Current: {current:.2f} A")
    elif choice == '3':
        print("\nSolving for RESISTANCE")
        voltage = float(input("Enter the voltage in Volts: "))
        current = float(input("Enter the current in Amperes: "))
        resistance = voltage / current
        print(f"Resistance: {resistance:.2f} Ω")
    else:
        print("Invalid input. Please enter 1, 2, or 3.")
except ZeroDivisionError:
    print("Sorry! Cannot divide by zero.")


# Exercise 3:  Diamond Shape (advance topic):
n = int(input("Enter a number: "))

if n % 2 == 1:
    for i in range(1, n+1):
        i = i - (n//2 +1)
        if i < 0:
            i = -i
        print(" " * i + "*" * (n - i*2) + " " * i)
else:
    print("Please provide an odd integer.")
