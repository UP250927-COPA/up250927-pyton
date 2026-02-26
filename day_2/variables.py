# variables.py
#Level 1
# Variables in Python
first_name = 'Cesar'
last_name = 'Perez Avila'
full_name = 'Perez Avila Cesar Omar'
country = 'Aguascalientes'
city = 'Aguascalientes'
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = True
age = '20'
year = '2026'
is_married = 'False'
is_true = 'True'
is_light_on = 'True'
name, age, country = 'Cesar', 20, 'Aguascalientes'
print ('first_name:', first_name)
print ('last_name:', last_name)
print ('full_name:', full_name)
print ('country:', country)
print ('city:', city)
print ('age:', age)
print ('year:', year)
print ('is_married:', is_married)
print ('is_true:', is_true)
print ('is_light_on:', is_light_on)
#Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type((name, age, country)))
type (first_name)
type (last_name)
type (full_name)
type (country)
type (city)
type (age)
type (year)
type (is_married)
type (is_true)
type (is_light_on)
data1 = "first_name"
data2 = "last_name"
if len (data1) > len (data2):
    print (f"{data1} is longer than {data2}")
elif len (data1) < len (data2):
    print (f"{data2} is longer than {data1}")
else:  
    print (f"{data1} and {data2} are of equal length")
num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division= num_one / num_two
print(division)
remainder= num_one % num_two
print(remainder)
exp = num_one ** num_two
print(exp)
floor_divission = num_one // num_two
print(floor_divission)
print ('The area of a is a circle with radius 30')
area_of_circle = 3.14 * 30 ** 2
print(area_of_circle)
print ('The circumferance of a circle with radius 30')
circum_of_cicle = 2 * 3.14 * 30
print(circum_of_cicle)
print('insert the radius')
radius = float(input("Enter the radius of a circle: "))
area = 3.1416 * radius ** 2
print('the area of the circle is: ', area)
print('give me the following information')
name = input("What is your name? ")
last_name = input("What is your last name? ")
country = input("What is your country? ")
age = input("What is your age? ")
print(f"Your name is {name} {last_name}, you are from {country} and you are {age} years old.")
help('keywords')