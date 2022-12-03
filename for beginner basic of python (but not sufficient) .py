print('hello world')
if 4 > 3:
        print('four greater than 3')
        print('hello world')
        print('hello')


#     for python and html also in vs code mein comment likhne ke liye hame only (ctrl+forward slash) dabana hai


# what is the syntax?

# sorted(data.values())
# where data is dictionary
# there are couple of ways as well.





x = 10
print(x)
y = 'hello'# strings
print(x)

x = 10
x = 'hello world'
print(x)

x ='hello world'
x = 10;
print(x)

x = 10
print(x)
x = 11
print(x)


  # PYTHON IS A CASE SENSETIVE LANGUAGE .

x=10
print(x)
print(type(x))

y = 'hello'
print(y)
print(type(y))

z = 3.78
print(z)
print(type(z))

x = 10
g = 6
print(x,g)


x = 10
g = 6
print(x+g)

a = 19
A = 20
print(a)

a = 19
A = 20
print(A)

x = 10
print(x)

x = 10;
print(x)

x=10
print(x)

# casting

x = str(10)
y = int(10)
z = float(10)
print(x,y,z)

#x = str(10)
#y = int(10)
#print(x+y)

x = int(10)
y = float(10)
print(x+y)
print(type(x+y))

#name
#age
#total_price
#_rishabh_gupta
#rishabh gupta
#4rishabh # error
#rishabh4
#name Name NAME

myname = 'rishabh'
print(myname) 

my_name = 'rishabh'
print(my_name)

_my_name = 'rishabh'
print(_my_name)

MYNAME = 'RISHABH'
print(MYNAME)

myname3 = 'rishabh'
print(myname3)

#2myname = 'rishabh'
#print(2myname) # error

#my-name = 'rishabh'
#print(my-name)

#my name = 'rishabh'
#print(my name)

x = 10
y = 20
z = 30
print(x)
print(y)
print(z)

x = 10
y = 20
z = 30
print(x,y,z)

x,y,z = 10,20,30
print(x)
print(y)
print(z)

x = y = z = 10
print(x)
print(y)
print(z)
print(x,y,z)

x = 'my name is rishabh'
print(x)

x = 'my'
y = "name"
z = "is"
s = 'rishabh'
print(x+' '+y+' '+z+' '+s)

x = 'my'
y = 'name'
z = 'is'
s = 'rishabh'
print(x,y,z,s)

x = 'my'
y = 'name'
z = 'is'
print(x+y+z)

x = 'my '
y = 'name '
z = 'is'
print(x+y+z)

x = 5
y = 10
print(x+y)

#x = 'hello'
#y = 10
#print(x+y)

x = 'hello'
y = 10
print(x,y)

x = 'rishabh'
def myfunc():
        print('my name is '+ x)
print(x)
myfunc()

x = 'john'
def myfunc():
        x = 'peter'
        print('my name is ' + x )
myfunc()
print(x)

x = 'john'
def myfunc():
        x = 'peter'
        print('my name is ' + x )
print(x)
myfunc()

x = 'john'
def myfunc():
        y = 'peter'
        print('my name is '+y)
myfunc()
print("my name is "+x)

x = 'john'
def myfunc():
        y = 'peter'
        print('my name is '+x)
myfunc()
print("my name is "+x)

#x = 'john'
#def myfunc():
#       y = 'peter'
#       print('my name is '+x)
#myfunc()
#print("my name is "+y)

y = 4+5j
print(y)

y = 4+5j
print(type(y))

  ##### LIST

x = [10,20,30]
print(x)
print(type(x))

# LIST IS ORDERED , COLLECTION OF SIMILIAR  or different DATATYPE.

x = [10,20,30]
print(type(x))

x = [10 ,20 ,"hello"]
print(x)
print(type(x))

# LIST OF INDEX

x = [10,20,"hello"]
print(type(x))
print(x[0])
print(x[1])
print(x[2])

# index start from zero.
# positive index (0,1,2,3......)
# negetive index (......-3,-2,-1)

x = '''Lorem ipsum is placeholder
 text commonly used in the graphic, print, and 
publishing industries for previewing 
layouts and visual mockups.'''
print(x)

x = """Lorem ipsum is placeholder text commonly used in the graphic, print, and 
publishing industries for previewing layouts and visual mockups."""
print(x)

a = "hello world"
print(a[0])
print(a[1])
print(a[2])
print(a[4])
print(a[3])


for x in "hello world":
        print(x)

a = 'hello'
print(len(a))

a = "hello world"
print(len(a))  # it's also count the space .

a = '''Lorem ipsum is placeholder
 text commonly used in the graphic, print, and 
publishing industries for previewing 
layouts and visual mockups.'''
print(len(a))

a = """Lorem ipsum is placeholder
 text commonly used in the graphic, print, and 
publishing industries for previewing 
layouts and visual mockups."""
print(len(a))

# LOOP METHOD

x = "we are studying python"
print("are" in x ) # TRUE

x = "we are studying python"
print("is" in x ) # FALSE
# range(slicing part)--
# for slicing the string or substrings--
# get the charater from position 2 to 5  , aac. to below , but 5 character not included
a = "helloworld"
print(a[2:5]) # (n-1) for slicing part for last index, who not come range(slicing part) , so it's give to run , llo

a = "hello world"
print(a[0])

a = "hello world"
print(a[0:5])

a = "hello world"
print(a[:5])

a = "hello world"
print(a[6:])

a = "hello world"
print(a[5:])

a = "helloworld"
print(a[5:])

a = "hello world"
print(a[2:])

a = "hello world"
print(a[-4:-1])

a = "hello world"
print(a[-4:])

a = "hello world"
print(a[-4:-2])

  # modify strings in python using set of built-in method
        # UPPER CASE METHOD
x = "Hello world"
print(x)
print(x.upper())

x = "RISHABH gupta"
print(x)
print(x.lower())


x = "hi everyone"
print(x)
print(x.upper())


## REMOVE WHITE SPACE . -----
   # strip method
x ="    lets study python"
print(x)
print(x.strip())

x ="                    we are studying python language"
print(x)
print(x.strip())

## replace method----
x = "hello world"
print(x.replace('h','ll'))

x = "hello world"
print(x.replace('h','A'))

x = "hello world"
print(x.replace('ello','xgyu'))

 #### SPLITTING A STRING-----

x ="hello world"
print(x.split())  ## AFTER RUN WE GET SUB STRINGS.

x ="hello world"
print(x.split()[0])

x ="hello world"
print(x.split()[1])

#x ="hello world"
#print(x.split()[2])  ## ERROR , list out of range

x ="hello world"
print(x.split(","))

x ="hello world"
print(x.split(','))


x ="hello world"  # x like a string.
y = x.split()  # y like a array.
print(y)
print(y[0])
print(y[1])

x ="hello world"
y = x.split()
print(x,y)

x = "hello world"
y = x.split()
print(x[0],y[0])

    #### how we can add the strings.( i.e. combined them )
           ## string concatenation.
x="hello"
y=" world"
z=x+y
print(z)

x="hello"
y="world"
z=x+y
print(z)

x = "hello"
y = "world"
z = x + " " +y
print(z)

    #### BOOLEAN DATA TYPE
print(2<5)
print(4>8)

## we need to check if a any expression if any code that we are writing is 'true' $ 'false'

print(5>2)

print(5==3)
print(5==5)

print(bool(20))
print(bool("hello"))
  ## any strings will return true except empty

print(bool(""))
print(bool(" "))
print(bool(0))
print(bool(1))
print(bool(22))

# print(bool(false)) # error
print(bool(False))

print(bool(""))
print(bool(()))
print(bool({}))
print(bool([]))
print(bool(0))


list = [10,20,30,40]
print(list)
print(type(list))

x = [1,2,3,4]
print(x)
print(type(x))

list_items = [10,20,30,40,"apples","oranges"]
print(list_items)
print(type(list_items))

list = [10,20,30,40,30,20]
print(type(list))
print(list) # also gives the duplicate value in list .

list__items = [10,20,30,40,50]
print(list__items)
print(list__items[0])
print(list__items[1])
print(list__items[2])
print(list__items[3])
print(list__items[4])
# print(list__items[5])  # error - list index out of range

#list = [10,'abcd',True,60,'apples']
#print(list)

#x=list((10,20,30))
#print(x)
#print(type(x))  ## it run , and give the ans. , but uske liye new file me ho jayega

listtwo = [10,20,30]
print(listtwo)
print(type(listtwo))

####  ACCESS THE LIST ITEMS--
list = [10,20,30,40,50]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[2:4])
print(list[:4])
print(list[2:])
print(list[2:6])

#### CHANGE THE LIST ITEMS----

list1 = [30,40,50,60]
list1[1] = 50
print(list1)


list1 = [30,40,50,60,80]
list1[1] = 'hello'
list1[4] = 'everyone'
print(list1)

####### CHANGE A RANGE OF LIST ITEMS----,

list1 = [30,40,50,60,70]
list1[1:2] = ['hi','hello']
print(list1)

list1 = [30,40,50,60,70,80,90,100]
list1[1:4] = ['hi','hello']
print(list1)

list1 = [30,40,50,60,70,80,90,100]
list1[1:4] = ['hi','hello',2,4,2,3,5]
print(list1)

####  INSERT ITEMS METHOD IN LIST METHOD----
list1 = [10,20,30]
list1.insert(2,'hello')
print(list1)

#### append items----
#### for adding the items at the end of the list
list1 = [10,20,30]
list1.append(40)
print(list1)

#list1 = [10,20,30]
#list1.append(40,'hello','hi')
#print(list1)  # error

list1 = [10,20,30]
list1.append(40)
list1.append('hello')
list1.append('hi')
list1.append('everyone')
list1.append('king')
print(list1)

#######  EXTEND THE LIST.

list1 = [10,20,30]
list2 = [40,50,60]
list1.extend(list2)
print(list1)
print(list2)

list1 = [10,20,30]
list2 = [40,50,60]
list2.extend(list1)
print(list1)
print(list2)

list1 = [10,20,30]
list2 = [40,50,60]
list2.extend(list2)
print(list1)
print(list2)

###### EXTENDED METHOD IN LIST WITH TUPLE.
list1 = [10,20,30,40]
tuple = (50,60)
list1.extend(tuple)
print(list1)

list1 = [10,20,30,40]
dictionary = {50,60}
list1.extend(dictionary)
print(list1)


##### REMOVEING A SPECIFIED ITEM FROM THE LIST
# remove()
mylist = [10,20,'hi',40]
mylist.remove(20)
print(mylist)

###### REMOVE ITEM FROM SPECIFED INDEX.
    # pop()
mylist = [10,20,'hi',40]
mylist.pop(2)
print(mylist)

my_list = ['john','peter','raj']
my_list.pop(2)
print(my_list)

#my_list = ['john','peter','raj']
#my_list.pop(3)
#print(my_list)  # error

my_list = ['john','peter','raj']
my_list.pop()
print(my_list)

my_list = ['john','peter','raj']
my_list.pop()
my_list.pop()
print(my_list)

my_list = ['john','peter','raj']
my_list.pop()
my_list.pop()
my_list.pop()
print(my_list)

  #### REMOVE ITEM FROM SPECIFIED INDEX USING del KEYWORD.

my_list = ['john','peter','raj']
del my_list[1]
print(my_list)

my_list = ['john','peter','raj']
del my_list[0]
del my_list[1]
print(my_list)

####  EMPTY THE LIST - USE  clear method

mylist = ['john','peter','raj']
mylist.clear()
print(mylist)

#####  LOOPING THROUGH THE LIST --
mylist = [10,30,20,40]
for x in mylist:
        print(x)

mylist = 'hello world'
for x in mylist:
        print(x)

#### LOOP THROUGH THE INDEX----
mylist = [10,20,30,40,]
print(len(mylist))
print(range(len(mylist)))

mylist = [10,20,30,40,50]
length = len(mylist)
range_of_my_list = range(length)
print(range_of_my_list)
for x in range_of_my_list:
        print(x)
for x in range_of_my_list:
        print(mylist[x])
#mylist = [10,20,30,40,50]
#print(range(mylist))  # error

mylist = [10,20,30,40,50]
print(range(len(mylist)))

##### LIST SORTING METHOD----
    ## sort in alpha numeric order default it is assending.
my_list = [ 'banana','orange','apple','guava']
my_list.sort()
print(my_list)

mylist = [10,20,400,30,12]
mylist.sort()
print(mylist)

  ####### SORT IN DECENDING ORDER

mylist = [90,400,200,20,10,50]
mylist.sort( reverse = True)
print(mylist)
 ## Accending ----
mylist = [90,400,200,20,10,50]
mylist.sort( reverse = False)
print(mylist)

  ####### CASE SENSETIVE SORTING BY DEFAULT SORT() IS CASE SENSETIVE
  # ALL THE CAPITAL letters will be sorted before lowercase letters.
mylist = ['banana','Orange','Apple','guava']
mylist.sort()
print(mylist)

mylist = ['banana','Orange','Apple','guava']
mylist.sort(key=str.lower)
print(mylist)

##### REVERSE THE ORDER OF A LIST

mylist = ['banana','orange','apple','guava']
mylist.reverse()
print(mylist)

## COPING THE LIST
list1 = [10,20,30]
list2 = list1
print(list2)

list1 = [10,20,30]
list2 = list1
list2.pop()
print(list2)

list1 = [10,20,30]
list2 = list1
list2.pop()
print(list1)

#### list also ordered.
# list also can have duplicates.

list1 = [10,20,30,40] # ORIGINAL LIST
list2 = list1.copy()# COPY LIST
print(list2)
list2.pop()
print(list1)
print(list2)

list1 = [10,20,30,40]
list2 = list1
print(list2)

####### ANOTHER WAY FOR COPING OF THE LIST .

list1 = [10,20,30,40]
list2 = (list1)
print(list2)
list1.pop()
print(list1)
print(list2)

# TUPLES ARE UNCHANGABLE
my_tuple = (10,20,30,40)
print(my_tuple)
print(my_tuple[0])

#mytuple=(10,20,30)
#mytuple[1] = 100
#print(mytuple) # error
  ## tuple are unchangable.

mytuple=(10,20,30,40)
print(len(mytuple))

mytuple = (10)
print(mytuple)
print(type(mytuple))

mytuple = (10,)
print(mytuple)
print(type(mytuple))

 # tuple constructor
#mytuple = tuple((10,20,30,40))
#print(mytuple)

mytuple = (10,20,30,40,50)
print(mytuple[3])
print(mytuple[-1])
print(mytuple[-2])

mytuple = (10,20,30,40,50)
print(mytuple[3:4])
print(mytuple[:4])
print(mytuple[-3:-1])

#mytuple = (10,20,30,40)
#mylist = list(mytuple)
#print(mylist)
#print(type(mylist))

#mytuple = (10,20,30,40)
#mylist = list(mytuple)
#mylist[2] = 200
#mytuple = tuple(mylist)
#print(mytuple)

##### APPEND TUPLE WITH ANOTHER TUPLE .

mytuple = (10,20,30,40)
x = (50,)
mytuple+=x
print(mytuple)

mytuple = (10,20,30,40)
x = (5,)
mytuple=mytuple+x
print(mytuple)

####### ESCAPE SYNTEX ----
a = "\U0001f601"
print(len(a))

a = "U0001f601"
print(len(a))

#text = 'it's alright'
#print(text) # error

text = 'it\'s alright'
print(text)

a = "\U0001f601"
for char in a:
        print(char)

tuple1 = (10,20,30)
del tuple1
print(tuple1)






# if we talk about print 
# then now for print , print hone wala one line mein hona chaiye to hum print('print hone wala part ')  use karte hai. 
# then now for print , print hone wala one  line mein na  ho to hum print('''print hone wala part''')  use karte hai.

print('hello world')  # it gives the value     hello world


print('''hello
world''')      # then it gives the value       hello
               #                               world   

#  if i want to print single downward slash   ( \ )    then we print  according to below method -
print('\\')        



# second method for if I print('hello rishabh') , and then I want to in this hello upper hi rah jaye and rishabh niche ki line mein chale jaye. 
# so we do according below method 

# print('hello \n rishabh')    after this we find   the value                 hello
#                                                                              rishabh
