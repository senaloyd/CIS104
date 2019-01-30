# Homework/Lab 2 Part 1
age = int(input("Enter your age: "))
age_ten = age + 10
print("In ten years you will be", age_ten, "years old.")
# Success! I was able to get it to round when it prints in Celsius.
ftemp = float(input("Enter the temperature in Fahrenheit: "))
ctemp = float((ftemp - 32) * 5/9)
print("The temperature in degrees Celsius is", "{:.2f}".format(ctemp))