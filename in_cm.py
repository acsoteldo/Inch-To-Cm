# Program to convert between centimeters and inches

# Constant conversion factor
INCH_TO_CM_FACTOR = 2.54

# Get input from the user in the form "number unit"
input_str = input("Enter a positive integer number and a unit (either 'cm' or 'in'): ")

# Split the input into two parts: the number and the unit
parts = input_str.split()

# Get the number and the unit from the input
number = float(parts[0])
unit = parts[1]

# Convert the number based on the unit
if unit == "cm":
  result = number / INCH_TO_CM_FACTOR
  result_unit = "in"
elif unit == "in":
  result = number * INCH_TO_CM_FACTOR
  result_unit = "cm"
else:
  print("Invalid unit")

# Print the result
print("{}{} = {:.1f} {}".format(number, unit, result, result_unit))
