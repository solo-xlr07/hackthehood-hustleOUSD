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

#Step 2
def total_price(item1, item2):
    total_sum = menu.get(item1) + menu.get(item2)
    return total_sum

print(total_price('Pizza', 'Burger')) #calling fucntion

#Step 3 (Mine)
def price_difference(item1, item2):
    total_sub = menu.get(item1) - menu.get(item2)
    if total_sub >= 0:
        return total_sub
    else:
       total_sub = total_sub * -1
       return total_sub

print(price_difference('Burger', 'Pizza'))

#Step 3 (Alterate)
def price_difference(item1, item2):
    total_difference = abs(menu[item1] - menu[item2])
    return total_difference

print(price_difference('Burger', 'Pizza'))

#Step 4
def inflation(item,number):
    new_price = menu.get(item) * number
    menu[item] = new_price  
    return menu

print(inflation('Churro', 4))


#Step 5
def defelation(item,number):
    new_price = menu.get(item) / number
    menu[item] = new_price  
    return menu

print(defelation('Churro', 4))

#Step 6
def cost(item):
    if item in menu:
        item_cost = menu[item]
        message = f'The cost of a {item} is ${item_cost}'
        return message
    else:
        no = 'not in menu'
        return no

print(cost("Burger"))
