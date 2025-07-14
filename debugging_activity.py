# DEBUGGING ACIVITY: Nelson Perez-Cordova (Hustle OUSD)

#CODE SNIPPET 1 
print('-----Case 1:-----')
x = 10
y = 2  #error
result = x / y
print("Result:", result)
#In line 6, y=0. We can't divide by 0: Change 0 to a 2

#CODE SNIPPET 2
print('-----Case 2:-----')
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i]) #error
#We want to access al the lists value. i+1 didnt let us so I removed the +1,
#therefore we can access each other.

#CODE SNIPPET 3
print('-----Case 3:-----')
def calculate_area(radius):
   area = 3.14 * radius ** 2 
   return area
 
radius = 5
print(calculate_area(radius))
#Added colons on line 21 where the function is being called

#CODE SNIPPET 4
print('-----Case 4:-----')
def is_even(number):
   if number % 2 == 0:  
       return True
   else:
       return False
 
print(is_even(4)) 
print(is_even(7))
#Added colons on line 32 for if statement to work

#CODE SNIPPET 5
print('-----Case 5:-----')
for i in range(5): 
   print(i) 
#Added colong on line 43 for for loop to work

#CODE SNIPPET 6
print('-----Case 6:-----')
def greet(name):
   return f"Hello, {name}" 
 
print(greet("Alice"))
#Change for name would be a varible thefore allowing its value to be printed

#CODE SNIPPET 7
print('-----Case 7:-----')
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
   sum += number #Moved line of code to be under the for-loop
print("Sum of numbers:", sum)

#CODE SNIPPET 8
print('-----Case 8:-----')
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1) #We desending so we subtracting not adding
 
print(factorial(5))

#CODE SNIPPET 9
print('-----Case 9:-----')
name = input("Enter your name: ")
if name == "Alice" or name == "Bob": #Change
   print("Hello, " + name)
else:
   print("Hello, stranger!")
#Change the or-statement in line 76

#CODE SNIPPET 10
print('-----Case 10:-----')
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 2 #Cant divide by 0
print(divide_numbers(num1, num2))
