 # LOOPS
 # WE HAVE while loop and for loop

 # IN PYTHON AND IN PROGAMMING LANGUAGE ,,   MEANING OF loop - REPEATING STATEMENTS

 # IF I TALK ABOUT GENERIC LOOP TERM , MEANING OF LOOP - SOMETHING THAT RUNS CONTINUOUSLY
# AND THE THINGS THAT ARE REPEATing AGAIN AND AGAIN IS loop .

# print number between 1 to 6 without loop.
print(1)
print(2)
print(3)
print(4)
print(5)

print('hello world')

#x = 1
#while x < 6:
#    print(x)    # it will give the repeating 1 .

x = 1
while x < 6:
    print(x)
    x = x + 1

print('AFTER')

x = 1
while x < 6:
    print(x)
    x += 1  # this is the assignment operator.

# PYTHON ASSIGNMENT OPERATOR - BELOW GIVEN LINK OF THIS OPERATOR ,
#  https://www.w3schools.com/python/gloss_python_assignment_operators.asp#:~:text=%E2%9D%AE%20Python%20Glossary-,Python%20Assignment%20Operators,Try%20it%20%C2%BB,-Related%20Pages

print('AFTER')

x = 8
while x < 6:
    print(x)

print('AFTER')

x = 7
while x < 6:
    print(x)
else:
    print(x+2)

x = 1
while x < 10:
    print(x)
    x += 1

#  break statement for loop

x = 1
while x < 10:
    print(x)
    if x ==6:
        break
    x += 1

# continue for loop


#x = 1
#while x < 10:
#    print(x)
#   if x == 6:
#       continue
#    x += 1         # IT IS AFTER 6 THIS IS continue IT MEANS THIS IS BECOME REPEATING STATEMENT .


x = 1
while x < 10:
    x += 1
    if x == 6:
        continue
    print(x)  # then it give the value 2 to 10 except 6

x = 0
while x < 10:
    x += 1
    if x == 6:
        continue
    print(x)   # then it give the value 1 to 10 except 6



# continue
x = 0
while x < 10:
    x += 1
    if x == 6:
        continue  # you skip the current iteration and move on to the next.
    print(x)

print('hello world')

x = 0
while x < 10:
    x += 1
    if x % 6 == 0:
        continue
    print(x)

    print('hello world one')

x = 0
while x < 20 :
    x += 1
    if x % 6 == 0:
        continue
    print(x)

print('hello rishabh')

# x = 0
# while x < 100:
    # x += 1
    # print(x)

# x = 1
# while x < 10:
    # print(x)
    # if x == 2:
        # continue
    # print(x)
    # x += 1

x = 0
while x < 100:
    x += 1
    if x - 6 == 0:
        continue
    print(x)

print( ' SEPERATE ')


x = 0
while x < 20:
    x += 1
    print(x)

print( ' SEPERATE one ')

x = 0
while x < 20:
    x += 1
    print(x)
else:
    print('out of range')




































