x = 40
y = 60
z = 80
if(x<y):
    print('true')


x = 40
y = 60
z = 80
if(x<y):
    print('true')
elif x == y:
    print('both number are same')

x = 70
y = 60
z = 80
if(x<y):
    print('true')
elif x == y:
    print('both number are same')

x = 60
y = 60
z = 80
if(x<y):
    print('true')
elif (x == y):
    print('both number are same')

x = 40
y = 60
z = 80
if(x<y):
    print('true')
else:
    print('false')

x = 70
y = 60
z = 80
if (x < y):
    print('true')
else:
    print('false')

x = 60
y = 60
z = 80
if (x < y):
    print('true')
else:
    print('false')

x = 80
y = 60
z = 80
if(x<y):
    print('true')
elif (x == y):  # if  if condition is not true then it checks for elif condition
    print('both number are same')
else:  # it will take all of the rest conditions except preceding ones
    print('no')

 #  multiple condition in a single line

 # AND and OR OPERATOR    # THIS OPERATOR IS LOGICAL OPERATOR.

x = 10
y = 20
z = 100
if (x<y and y<z):
    print('hello')

x = 200
y = 20
z = 100
if (x<y and y<z):
    print('hello') #  ITS GIVES NOTHING .

#   FOR     'and'      'BOTH THE CONDITIONS IS TRUE'
#   FOR     'or'       'AT LEAST ONE CONDITION IS MET'
x = 200
y = 20
z = 100
if (x<y or y<z):
    print('hello')




# NESTED if-else conditions

x = 40
if(x < 60):
    print('x is less than 60')
    if(x > 50):
        print('x is greater than 50')

x = 40
if(x < 60):
    print('x is less than 60')
    if(x < 50):
        print('x is also less than 50')

x = 40
if(x < 60):
    print('x is less than 60')
    if(x < 50):
        print('x is also less than 50')
    else:
        print('false')

x = 55
if(x < 60):
    print('x is less than 60')
    if(x < 50):
        print('x is also less than 50')
    else:
        print('false')

x = 70
if(x < 80):
    print('x is also less than 50')
    if(x < 60):
        print('x is less than 60')
    else:
        print('false')
print('hello world')

x = 70
if (x < 60):
    print('x is less than 60')
    if(x < 80):
        print('x is also less than 50')
    else:
        print('false')

x = 70
if (x < 60):
    print('x is less than 60')
    if(x < 80):
        print('x is also less than 50')
else:
    print('false')

print('hello world')
x = 70
if (x < 60):
    print('x is less than 60')
    if(x < 50):
        print('x is also less than 50')
    else:
        print('x is either equal or greater than')
else:
    print('false')



x = 70
if (x < 80):
    print('x is less than 80')
    if(x < 50):
        print('x is also less than 50')
    else:
        print('x is either equal or greater than')
else:
    print('false')



#x = 20
#if(x < 40):

#else:
 #   print('x is less than 40')  #  ERROR

print('hello world')


x = 20
if(x < 40):
    pass
else:
    print('x is less than 40')


x = 60
if(x < 40):
    pass
else:
    print('x is less than 40')

    





