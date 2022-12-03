#  functional programming and oops (object oriented programming)

# python is an oops language 
# object is nothing but a collection of data 
# Classes are used to create one or more objects 

# class MyClass:
#     a = 40

# print(MyClass)   



#   creat an object 

# class MyClass:
#     a = 40

# object1 = MyClass()
# print(MyClass) 



# class MyClass:
#     a = 40

# object1 = MyClass()
# print(MyClass.a) 




# class MyClass:
#     a = 40

# object1 = MyClass()
# object2 = MyClass()
# print(object1.a,object2.a)



#  __init__() => all classes have this prebuilt function  which is always executed when the class is being initiated.

# class person:

#     def __init__(self , name , age):
#         print(name,age)

# person1 = person('john', 40)        
# person2 = person('peter', 20  )



# class person:
#     def __init__(self, name, age):

#      self.name = name
#      self.age = age 

# person1 = person('john',40)
# person2 = person("peter", 20)
# print(person1.name)    
# print(person2.name)  



# object methods 

# class person:
#     def __init__(self , name , age):

#         self.name = name
#         self.age = age 

#     def myFunc(self):
#         print('My name is ' + self.name)

# person1 = person('john', 40)
# person2 = person('peter',20)

# print(person1.myFunc())
# print(person2.myFunc())



class person:
    def __init__(self , name , age):

        self.name = name
        self.age = age 

    def myFunc(self):
        print('My name is ' + self.name)

person1 = person('john', 40)
person2 = person('peter',20)

person1.myFunc()
person2.myFunc()

myList = [10,20,30]
myList.append(40)
print(myList)


# the refrence top the current instance of the class will always be the first parameter of the function that you define inside the class. 

class person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
person1 = person('john', 40)  
person2 = person("peter", 20)      

person2.age = 10
# print(person1.name)
print(person2.name)
print(person2.age)

del person1
print(person1)





class person:
    pass



class User:
    def __init__(self , firstName , lastName):
        self.firstName = firstName 
        self.lastName = lastName

user1 = User('john','rishabh')
print(user1.firstName)     
       



# INHERITANCE 
# parent class(base class) and child class(derived class )
# user class => student , programmer , teacher some common property like name 




#parent class
class User:
    def __init__(self , firstName , lastName):
        self.firstName = firstName
        self.lastName = lastName 
    def printName(self):
        print(self.firstName, self.lastName)
user1 = User('john',"rishabh")

#child class 
# inherits the properties and functionality from another class 
class student(User):
    pass

student1 = student('mike', 'tyson')
student1.printName()







class User:
    def __init__(self , fName , lname):
        self.firstName = fName
        self.lastName = lname 
    def printName(self):
        print(self.firstName, self.lastName)
user1 = User('john',"rishabh")

class student(User):
    pass

student1 = student('mike', 'tyson')
student1.printName()







class User:
    def __init__(self , fname , lname):
        self.firstname = fname
        self.lastname = lname 

    def printName(self):
        print(self.firstname, self.lastname)

user1 = User('john',"rishabh")

class student(User):
    def __init__(self, fname, lname):
        self.firstname = lname
        self.lastname = fname 

student1 = student('mike', 'tyson')
student1.printName()

















































