# Data Science is broken up into Data wrangling, analytics, predictions
# Datatypes: Integer, Float(decimal), Strings, Boolean, None(Undefined)
# Variables are written in camelCase or snake_case, so their names can include special characters(e.g letters, numbers, underscores)
# Data Structures: Lists and Dictionaries:
#     -List (Array) = ["hello","world"];
#     -Dictionary (Object) = {
#         first_word: "Hello",
#         second_word: "World"
#         }
# Lists can have multiple data types within it:
#     random_list = ["Matt", 2, 3.14, true]

# Django is backend for web applications

print("Hello World")

my_name = "Matthew"

print(my_name)

type(my_name)

pizza_toppings = ["pepperoni", 2, "Sausage", "Green Olives"]

print(pizza_toppings)

car_dict = {
    "brand": "Toyota",
    "model": "4Runner",
    "year": 2008
}

print(car_dict)
type(car_dict)

print(car_dict["brand"])

# Functions:


def hello():
    name = str(input("Please Enter Your Name: "))
    if name:
        print("Hello " + str(name))
    else:
        print("Hello World")
    return


def birth_year():
    age = str(input("How old will you be this year?"))
    if age:
        year = 2018 - int(age)
        print("You will be " + year + " years old")
    else:
        print("Fine, be that way")
    return

    def circumferance(radius):
        cir = radius * 3.1415
        print(cir)

    circumferance(5)
    new_radius = 300
    circumferance(new_radius)

    def far_to_cel(fahrenheit):
        celsius = int((fahrenheit - 32) / 1.8)
        return(celsius)

        far_to_cel(66)
        new_degrees = 100
        far_to_cel(new_degrees)
