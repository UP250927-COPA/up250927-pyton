mpty_tuple = ()

sisters = ("Fatima")
brothers = ("Angel")

siblings = sisters + brothers

print("NUMBER OF SIBLINGS:", len(siblings))

family_members = siblings + ("Luis", "Maria")

print("FAMILY MEMBERS:", family_members)

*siblings, father, mother = family_members

print("SIBLINGS:", siblings)
print("FATHER:", father)
print("MOTHER:", mother)

fruits = ("Melon", "Watermelon", "Lemon")
vegetables = ("Garlic", "Corn", "Tomato")
animal_products = ("Chicken", "Eggs", "Fish")

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)

middle = len(food_stuff_lt) // 2
print("MIDDLE ITEM:", food_stuff_lt[middle])

print("FIRST ITEM:", food_stuff_lt[:3])

print("LAST THREE:", food_stuff_lt[-3:])


del food_stuff_tp

nordic_countries = ("DENMARK", "FINLAND", "ICELAND", "NORWAY", "SWEDEN")

print("IS ESTONIA A NORDIC COUNTRY?", "ESTONIA" in nordic_countries)
print("IS ICELAND A NORDIC COUNTRY?", "ICELAND" in nordic_countries)