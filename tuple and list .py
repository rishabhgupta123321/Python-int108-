mytuple = (10,20,30,40)
print(mytuple)

mytuple = tuple((10,20,30,40))
print(mytuple)



mytuple = (10,20,30,40)
mylist = list(mytuple)
print(mylist)
print(type(mylist))




mytuple = (10,20,30,40)
mylist = list(mytuple)
mylist[2] = 200
mytuple = tuple(mylist)
print(mytuple)