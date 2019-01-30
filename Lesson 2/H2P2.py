# Homework/Lab 2 Practice 2
book_title = input("Enter the book title: ")
author_name = input("Enter the name of the author: ")
publish_year = int(input("Enter the publish year of the book: "))
pages_total = int(input("Enter the total number of pages in the book: "))

current_year = 2019
book_age = current_year - publish_year

# 1st if-else statement 
if (book_age <= 10):
    print("This book is younger than ten years old.")
else:
    print("The book is at least ten years old.")

# 2nd if-elif-else statement
if (pages_total < 100):
    print("This book is a short book.")
elif (pages_total <= 300 >= 100):
    print("This book is an average book.")
else:
    print("This book is a long book.")