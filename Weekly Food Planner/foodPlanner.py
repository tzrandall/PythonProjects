from datetime import date
from random import choice
from person1 import person1Makes
from person2 import person2Makes

daysForMeals = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
groceryList = ['Water', 'Dr.Pepper', 'Snacks']
mealList = []

scheduleFile = open(str(date.today()) + '.txt', 'w')
groceryFile = open(f'grocery_list_for_{date.today()}.txt', 'w')

for day in daysForMeals:
    scheduleFile.write(str(day) + '\n')
    if day == 'Monday' or day == 'Wednesday':
        meal = choice(person1Makes)

    else: # day == 'Tuesday" or day == 'Thursday'
        meal = choice(person2Makes)

    mealList.append(str(meal[0]))
    for item in meal:
        if item not in mealList and item not in groceryList:
            groceryList.append(item)
            
    scheduleFile.write(str(meal[0]) + '\n\n')

for grocery in groceryList:
    groceryFile.write(str(grocery) + '\n')