#TASK 1
food = 'pupusas of beans and cheese'

print(food[0:3])  #first 3 charectors
print(food[-3:])  #last 3 charactors (-3: includes last one)

first_last = food[0]+food[-1]
print(first_last)

food_list = food.split()
print(food_list)

joined_food =' '.join(food_list)
print(joined_food) 

#TASK 2
number_list = [590, 2949, 20, 6, 17]

number_list.append(89)
print(number_list)

number_list.insert(3,"element")
print(number_list)

number_list.pop()
print(number_list)

number_list.remove(number_list[1])
print(number_list)

print(number_list[:3])  #first 3 charectors (left side blank = start from start)
print(number_list[-3:])  #last 3 charactors

#TASK 3
books = {
    'Scott Cawthon':'Fazbear Frights',
    "Micheal Crichton":"Jurric Park The Novel", 
    "Gregory Keyes":"Godzilla: King of the Monsters",
    "Jeff Kinney":"Diary of a Wimpy Kid"
    }

print(books.keys())                   #2
print(books.values())                 #3
print(books.get("Scott Cawthon"))     #4

books.pop('Gregory Keyes') 
print(books)

del books['Scott Cawthon'] 
print(books)