FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp = float(input("Enter the temperature to convert: "))
state = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if type(temp) == int or type(temp) == float:

    if state == "C:
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
    elif state == "F":
        print(f"{temp}°F is {convert_to_celsius(temp)}°C")
    else:
        print("Invalid input")
else:
    print("Invalid temperature. Please enter a numeric value.")