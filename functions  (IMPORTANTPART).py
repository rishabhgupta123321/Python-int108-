# function is predefined lines of codes
#  which do some specific task when it is called

# FUNCTION 

# A BLOCK OF CODE THAT IS EXECUTED WHEN IT IS CALLED 

# A FUNCTION EITHER DOES SOMETHING OR IT  RETURN SOMETHING
#   YOU CAN REUSE IT ANYWHERE IN YOUR CODE . 


# IN PYTHON , WE DEFINED THE FUNCTION WITH     def      keyword.   





# def my_func():
#     print('hello world')    THIS IS NOT GIVE ANYTHING , BEACAUSE ABHI ESE CALL NHI KARA HAI , WHEN WE CALL IT , THEN WORK . 
    # ABOVE KO CALL KARNE KE LIYE HAME USKE OUTSIDE MEIN     my_func()     LIKHNA HOGA , WHEN IT WORK. 

def my_func():
    print('hello world') 

my_func()



def my_func():
    print('hello one ') 

my_func()    
my_func()  
my_func()  
my_func()  
my_func()  
my_func()  




#  data into functions arguments 

def my_func(fNAME):
    print("hello world" + fNAME)

my_func(" rishabh ")   



def my_func(fNAME):
    print("hello world" + fNAME)



def my_func(fNAME , INAME ):
    print("hello world" + fNAME + INAME)

my_func(" rishabh","run")  
   #  my_func() takes 1 positional argument but 2 were given 




def my_func(fNAME , INAME ):
    print("hello world" + fNAME , INAME)

my_func(" rishabh","run")  



def my_func(fNAME , INAME ):
    print("hello world" + fNAME)

my_func(" rishabh"," run")   # THEN IT GIVES   hello world rishabh .


def my_func(fNAME , INAME ):
    print("hello world" + fNAME + INAME)

my_func(" rishabh","run")  



def my_func(INAME,fNAME):
    print("hello world" + fNAME + INAME)

my_func(" rishabh"," run")  



def my_func(INAME,fNAME , age ):
    print("hello world" + fNAME + INAME + ' ,my age is '+ age )

my_func(" rishabh"," run" , '18' )  









# FUNCTION - FUNCTION - FUNCTION - FUNCTION - FUNCTION.    


#  IN FUNCTION HUM REPEATATIVELY TASK KE BEECH MEIN EK SPECIFIC TASK KE LIYE FUNCTION SE WE CALL FUNCTION . 


# TASK1 
# TASK2
# TASK3 
# TASK4
# TASK5
# TASK6 
# TASK7
# TASK8

# ABOVE RULE LIKE  LOOP METHOD APPLY. 


# BUT SPECIFIC TASK IN BETWEEN LIKE THIS ----



# TASK1 
# TASK2
# TASK3 
# TASK4
# TASK2
# TASK5
# TASK2
# TASK6 
# TASK7
# TASK2
# TASK8


# THIS ABOVE METHOD LIKE THIS FUNCTION APPLICABLE , THEN WE CALLED FUNC. 
#   FUNCTION -----    IT IS  A  PIECE OF CODE THAT ONLY RUNS OR EXECUTE WHEN IT IS CALLED . 



def printText():
    print('hello world')
    print('hello')
    print('bye')


print(1)
printText()
print(2)
print(3)
print(4) 
printText()
print(5)
printText()
print(6)
print(7)

# WE ALWAYS TRY TO USE FUNCTION.
#  ONE FUNCTION IS ENOUGH ONLY.

# DATA INSIDE THE FUNCTION.

def printName():
    print('My name is '+ 'john')

printName()


def printName():
    print('My name is '+ 'john')
printName()




def printName():
    print('My name is '+ 'john')
printName()
printName()
printName()
printName()  # this is called the parameters.




def printName(name):
    print('My name is '+ name)

printName('john')
printName('rishabh')
printName('try')
printName('rahsy')  # this is called the arguments .


def printName(name , age):
    print('My name is '+ name + " and my age is "+ age)

printName('john' , '10')
# printName('rishabh')
# printName('try')
# printName('rahsy')



def printName(name , age):
    print('My name is '+ name + " and my age is "+ age)

printName('john' , '10')
printName('rishabh' , '32')
printName('try', '35')
printName('rahsy', '21')


def printSum(num1, num2):
    print(num1 + num2)

printSum(10, 20)    
printSum(20,40)    




# arbitrary arguments 

# when we  are not sure about the number arguments that can be passed inside 
# a function , add * to the parameter 



def myName(name):
    print('My name is ' + name )

myName('john')   

# def myName(name):
#     print('My name is ' + name )

# myName('john','peter','Raj')   # THEN IT GIVES THE ERROR .  





# def myName(name):
#     print('My name is ' + name[1] )

# myName('john','peter','Raj')      # then it gives the type error . 


#  FOR TUPLE BANE KE LIYE HUM NAME KE AAGE * LAGA DENGE .




# def myName(*name):
#     print('My name is ' + name )

# myName('john','peter','Raj')       # then it give the error beacause ye tuple to aa gya * lagane se  but yha konsa name ka argument dalna hai ye nhi pta hai . 


def myName(*name):
    print('My name is ' + name[1])

myName('john','peter','Raj') 



def myName(*name):
    print('My name is ' + name[2])

myName('john','peter','Raj') 



def myName(*name):
    print('My name is ' + name[0])

myName('john') 



# def myName(*name):
#     print('My name is ' + name[2])

# myName('john')   # then it give the error . 



def myName(*name):
    print('My name is ' + name[0])

myName('john')  



#  so because    *name   is like tuple .


def myname(*name):
    print('my name is '+ name[2])
    print(name)

myname('john','peter','Raj')        # it likes behave tuple.





  ####  IN TUPLE ----TUPLE DEFINATION --
  #  ORDERED AND UNCHANGABLE IS CALLED TUPLE 
  #  A SET CAN'T CONTAIN DUPLICATE VALUES.
#  A TUPLE CAN CONTAIN DUPLICATE VALUES.







# arguments based on key value.
# key words arguments 
# we can send the arguments in the form  key = value 
 


def myname(name1, name2, name3):
    print('my name is '+ name1 + name2 + name3)


myname(name1='john',name2='peter',name3='Raj')    




def myname(name2, name3, name1):
    print('my name is '+ name3)


myname(name1='john',name2='peter',name3='Raj')    



#   for ARBITRARY ARGUMENTS , we use * ( one star)
#    for ARBITRARY  KEYWORD ARGUMENTS , we use ** ( two star )




#  ARBITRARY  KEYWORD ARGUMENTS. 
#  ARBITRARY  KEYWORD ARGUMENTS is also called as   kwargs  .  and we use  **   for it   .
 


def myname(**name):
    print(name)


myname(name1='john',name2='peter',name3='Raj')     # then     **     dictionary data type hai , 



def myname(**name):
    print(name)


myname(name1='john',name2='peter',name3='Raj')   #  it gives the value in dictionary form . 





def myname(**name):
    print( 'my name is' + name['name1'] )


myname(name1=' john',name2='peter',name3='Raj')   



def myname(**name):
    print(name)
    print( 'my name is' + name['name2'] )


myname(name1=' john',name2=' peter',name3='Raj')   







def my_func(age):
    print('my age is '+ age )

my_func('10')





def my_func(age):
    print('my age is '+ age )

my_func('10')
my_func('20')





def my_func(age):
    print('my age is '+ age )

my_func('10')
my_func('20')
# my_func()    # then it give the type error .




## Default parameter value. 

def my_func(age = '40'):
    print('my age is '+ age )

my_func('10')
my_func('20')
my_func()




def my_func(age = '40'):
    print('my age is '+ age )

my_func('10')
my_func('20')
my_func()
my_func()
my_func()
my_func()


def printFruit(fruits):
    print(fruits)
    for fruit in fruits:
        print(fruit)
fruits=['apples','bananas','oranges']
printFruit(fruits)

#  till above we are only doing something.
# Functions either do something or return something.  
# if you want to return a value , you have return keyword.




def printAge():
    print(10)
    return(20)

printAge()



def printAge():
    return(20)

print(printAge())


def printAge():
    return(20)

    print(10)
print(printAge())


def printAge():
    print(10)
    return(20)

print(printAge())



def printAge():
    return(20)

    print(10)
    print(10)
    print(10)
    print(10)
print(printAge())



def printAge():
    print(10)
    print(10)
    return(20)

print(printAge())



def myFunc(x):
    print(x)
    return(2*x)
print(myFunc(5))
print(myFunc(6))





# Below link - questions based on functions and loops and conditions. --
#   https://docs.google.com/document/d/1fBmJrqs5ae1SNbn_9bRcSpBBIdKTENXBV-aDHYicykc/edit?usp=sharing    