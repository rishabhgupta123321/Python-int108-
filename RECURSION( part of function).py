# Recursion
# recursion topic also part of the function.

def square(num):
    return(num*num)
print(square(5))    

# any repeataion for we use recursion(part of function) and loop method .

def printNum(x):
    print(x)

def square(num):
    printNum(20)
    return(num*num)
    
print(square(2))        




def printNum(x):
    print(x)

def square(num):
    return(num*num)
    printNum(20)
print(square(2))



def printNum(x):
    print(x)

def square(num):
    printNum(20)
    return(num*5) 
   

def printNum(x):
    print(x)

def square(num):
    printNum(20)
    return(num*5)     # it will give nothing , beacause square function is not complete ,so it does not execute .   



def printNum(x):
    print(x)

def square(num):
    return(num*num)

printNum(20)
print(square(2))    



def printNum(x):
    print(x)

def square(num):
    printNum(20)   # called function.
    return(num*num)


print(square(2))  #calling function.





# it is also possible to call the function itself.

def printName():    # when a function called itself ,it is a process , it is called as recursion . 


    print('john')
    printName()     # this is kind of infinite loop . 

printName()    










# RECURSION
# recursion topic also part of the function.



# factorial 
# 5! => product of all integers from 1 to the number 
#   1 * 2 * 3 * 4 * 5 = 120 
#   3! => 1*2*3 = 6
#  2! => 1*2 = 2 



def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)

num = 5 

print("The factorial of given number", num,' is ',factorial(num))

# 5*factorial(4)
# 5*4*factorial(3)
# 5*4*3*factorial(2)
# 5*4*3*2*factorial(1)
# 5*4*3*2*1*factorial(0)
# 5*4*3*2*1*0*factorial(-1)

def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)

num = 6

print("The factorial of given number", num,' is ',factorial(num))




def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)

num = 1

print("The factorial of given number", num,' is ',factorial(num))



def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)

num = 0

print("The factorial of given number", num,' is ',factorial(num))



# you do not everything through , beacause recursion process is slow comparasion to loops , so as far as possible you should use loops , recursion like as a trick .
# recursion can make program slow, due to number of function calls taking place.




# question----
# we need to write a python program to find the power of a number using recursion 
# input : num = 2 , power = 3 
# output : 8    -------Answer ---->>>>



# num=int(input("number: "))
# p1=int(input("power: "))
# def func(n,p):
#     if p==1:
#         return n
#     else:
#         return n*func(n,p-1)
# print("output:",func(num,p1))