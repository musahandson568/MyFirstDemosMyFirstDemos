# print("My name is Handson")
# print("My name is Handson")
# age=26
# height=5.9
# name="Handson"
# print(f"My Name is {name} My age is {age} My height is {height}")
# #list
# cars=["Mercedes","Honda","Toyota","Audi","Volkswagen"]
# for car in "cars":
# print(cars)
 # print(f"The car is :{cars}")
# print(cars)
# length=[len(car) for car in cars]
# length={car:len(car) for car in cars}
# print(length)

# #input function
# name=input("Enter your name: ")
# email=input("Enter your email: ")
# phone_number=int(input("Enter your phone number: "))
# print(f"My name is {name} My email is {email} My phone number is {phone_number}")
#operators
# name=input("Enter your name : ")
# age=int(input("Enter your age :"))
# #assign
# current_year=2025
# year_user_turns_100=current_year + (100-age)
# print(f"My Name is {name} and I will turn 100 years old {year_user_turns_100}")

#control flow statement
# number=int(input("Enter a number: "))
# if number % 3==0 and number % 5==0:
#     print("FizzBuzz")
# elif number % 3==0:
#     print("Fizz")
# elif number % 5==0:
#     print("Buzz")
# else:
#     print(number)

# import subprocess
# from unittest import result
#
# data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
# profile = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
#
# for i in profile:
#     results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
#     results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#     try:
#         print("{:<3}|  {:<}".format(i, results[0]))
#     except IndexError:
#         print("{:<3}|  {:<}".format(i, "None"))
# input("\n\nPress enter to continue...")

class Criminal:
    def __init__(self, name, id_number, crime,gender):
        self.name = name
        self.id_number = id_number
        self.crime = crime
        self.gender= gender
    def show_details(self):
        print(f"Name: {self.name} \nID: {self.id_number} \nIssue: {self.crime}\nGender: {self.gender} ")


c1 = Criminal("Handson Musa", "36656413", "Expired Driving Licence", "Male")
c2 = Criminal("Jane Kamau", "34785917", "Selling Illegal Juice", "Female")
c1.show_details()
c2.show_details()

