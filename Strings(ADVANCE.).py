# Lets talk about strings --
# we have seen python string and modify string and format string.
# format strings

# age = 40
# print('My name is john. My age is ' + age)   # This is given error . 




# format()

age = 20 
text = 'My name is john. My age is {}'    # {} (curly braket) This is Kind of a place holder.
print(text.format(age))





# Let how many arguments you can use here .

quantity = 5 
items = 3 
money = 100 

text = 'The amount for these {} items is {} rupees. Total Quantity is {}'

print(text.format(items,money,quantity))


quantity = 5 
items = 3 
money = 100 

text = 'The amount for these {0} items is {1} rupees. Total Quantity is {2}'

print(text.format(items,money,quantity))


quantity = 5 
items = 3 
money = 100 

text = 'The amount for these {1} items is {0} rupees. Total Quantity is {2}'

print(text.format(items,money,quantity))


# Escape Characters

print('We are "good" players of football')

# print("We are "good" players of football")  # Error

print("We are \"good\" players of football")

print('Hello world')

print('Hello\nworld') # This is for new line.

# FOR STRINGS TYPES OF MANY METHOD . so you can look more string related methods.



text = 'it is a small method , you can write this.'
print(text.capitalize())  # in this part only first word part i is become capital I.

print('HELLO'.casefold())  # then it give hello.

print('My age is 20. MY lucky num is also 20'.count('20'))
print('My age is 20. MY lucky num is also 20'.count('is'))

print('My age is 20. MY lucky num is also 20'.endswith('20'))
print('My age is 20. MY lucky num is also 20'.endswith('.'))

print('My age is 20. MY lucky num is also 20'.find('age'))

print('My age is 20. MY lucky num is also 20'.find('z'))

print('My age is 20. MY lucky num is also 20'.index('age'))



text = 'My Name is JOHN'

print(text.swapcase())
