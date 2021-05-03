############DEBUGGING#####################

# # Describe Problem
#Broken:
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
##Function is supposed to print 'You got it' when 'i' equals 20, but 'i' cycles through the values and only goes up TO 20 without becoming 20. You can expand the range or change the value of i.
#Fixed:
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
#It SHOULD random choose an int and print the corresponding dice image, however the dice_imgs are in a list, and lists start from 0, not 1. This also means the final value would not be 6, but 5. It thus gives the error message "list index out of range" when hitting 6. You can REPRODUCE this bug by changing the value of randint tonumbers 1-6 in turn, and seeing which throw a bug..
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
#Fixed:
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
#Broken:
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
#
#The problem is that the if statements do not factor in if the input is  1994, only using it as limits. You can find this by taking a bugged input like 1994, and replacing it where "year" would be. By determining True and False statements, you can find if there is actually no True statement for that bugged input.
#Fixed
# year = int(input("What's your year of birth?"))
# if year = 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
#Here, the bugged line is marked in an editor with a red line. Hover over to find that it expected an indent (since it is after an if.) Even with that fixed, it throws another error about comparing between str and int, because the input is a str not an int. The output also fails to make an f string as it doesn't have an f.
#Broken:
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")

# #Print is Your Friend
#Broken:
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
#This bugs out by returning 0 as an answer. You can use Print to debug by printing the values directly after receiving input, seeing which value is causing the return of 0. Doing this, you can see that that the word_per_page is causing the issue and returning a 0 no matter what is entered. When you look at the code where it is input, you can see that it uses a double == instead of a single =, setting it to the originally defined 0. 
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# word_per_page = int(input("Number of words per page: "))
# # print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
#Broken:
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
#This is supposed to loop through the items in the a_list, times them by 2, then put them each in the b_list after. Running it through Python Tutor Debugger, we see it loops through the list and multiplies them by 2, but then immediately loops back to do the next number-- without adding it to the list. We can then look at the code and realize the call to put the new value in the b list is NOT in the loop, and we can indent it so it IS, causing each mutated number to be added to the b list.
#You can also pick a "break point" by clicking a line in Python Tutor, and it will tell you when it runs-- in the bugged version, it will show only one activation, towards the end.
#Fixed:
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)
# mutate([1,2,3,5,8,13])