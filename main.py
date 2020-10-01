print("Hello World")

# Python Program to Convert Kilometers to Miles
# In this example, we'll learn to convert kilometers to miles and display it.

# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
