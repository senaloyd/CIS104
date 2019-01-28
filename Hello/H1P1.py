first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
age = int(input("What is your age? "))
confidence = int(input("What is your confidence in programmers between 0-100%? "))
dog_age = int(age * 7)
print("Hello", first_name, last_name,", nice to meet you! You might be", age, "in human years, but in dog years you are", dog_age,".")
confidence_level = (confidence/100.0)
if confidence_level < 0.5:
    print("I agree, programmers can't be trusted!")
else:
    print("Writing good code takes hard work!")