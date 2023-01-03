# Inch-To-Cm

## hw

Write a Python program that converts between centimetres and inches. The pro-
gram asks the user to enter a single line of input containing a positive integer
number and a unit (either ’cm’ or ’in’) separated by a space e.g.

4 in

If the input is in inches, the program converts to the equivalent in centimetres and
prints the result in the following format

4in = 10.2 cm


The result should be displayed to one decimal place. (Centimetre inputs are con-
verted to inches and the result displayed in a similar fashion.) You may assume
that one inch is 2.54 centimetres.


### Notes
This program first gets input from the user in the form "number unit", where "number" is a positive integer and "unit" is either "cm" or "in". It then splits the input into two parts: the number and the unit.

Next, the program converts the number based on the unit using the conversion factor of 2.54. If the unit is "cm", it converts the number to inches, and if the unit is "in", it converts the number to centimeters. If the unit is neither "cm" nor "in", it prints an error message.

Finally, the program prints the result in the format "number unit = result result_unit". The result is displayed to one decimal place.
