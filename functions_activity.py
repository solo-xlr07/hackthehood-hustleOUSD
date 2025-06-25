#Step 1
menu = {
    'Pizza': 2.99, 
    'Burger': 3.99, 
    'Hot dog': 1.99, 
    'Cheese': 0.59, 
    'Ice cream': 1.49, 
    'Churro': 0.79, 
    'Soda': 0.89
} 

#Step 2 (1-2 Stretch done)
def total_price(item1, item2):
    if item1 and item2  in menu:
        total_sum = menu.get(item1) + menu.get(item2)
        message = f'The total cost is ${total_sum}' #stretch 1
        return message
    else: #stretch 2
        message_bad = "One or both items are not in the menu" 
        return message_bad

#print(total_price('Burger', 'Burger')) #calling function

#Step 3 (Mine) (Did all stretchs)
def price_difference(item1, item2):
    if item1 in menu and item2  in menu:
        total_sub = menu.get(item1) - menu.get(item2)
        if total_sub >= 0:
            message1 = f'The difference between {item1} and {item2} is ${total_sub}' 
            return message1
        else:
            total_sub = total_sub * -1
            message2 = f'The difference between {item1} and {item2} is ${total_sub}'
            return message2
    else:
        message_bad = "One or both items are not in the menu"
        return message_bad
        
print(price_difference('Burger', 'jss'))

#Step 3 (Alterate)
def price_difference(item1, item2):
    total_difference = abs(menu[item1] - menu[item2])
    return total_difference

#print(price_difference('Burger', 'Pizza'))

#Step 4
def inflation(item,number):
    if item in menu:
        new_price = menu.get(item) * number
        menu[item] = new_price  
        message_inflation = f'The price of a {item} is now ${new_price}'
        return message_inflation, menu
    else:
        message_bad_inflation = "Item is not in the menu"
        return message_bad_inflation
print(inflation('Churro', 4))


#Step 5
def defelation(item,number):
    if item in menu:
        new_price = menu.get(item) / number
        menu[item] = new_price  
        message_defelation = f'The price of a {item} is now ${new_price}'
        return message_defelation, menu
    else:
        message_bad_defelation = "Item is not in the menu"
        return message_bad_defelation

print(defelation('Churro', 4))

#Step 6
def cost(item):
    if item in menu:
        item_cost = menu[item]
        message = f'The cost of a {item} is ${item_cost}'
        return message
    else:
        no = 'Not in menu'
        return no

print(cost("Burger"))
