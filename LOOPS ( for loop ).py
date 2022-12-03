 # for loop

num = [10,20,30,40]
for x in num:
    print(x)

print("  ")

for x in 'hello':
    print(x)

#  BREAK IN FOR LOOP 

# num = [10,20,30,40]
# for x in num:
    # print(x)
    # if x ==30:
        # break
    # print(x)

# num = [10,20,30,40]
# for x in num:
    # print(x)
    # if x ==30:
        # break    
        

print('hello world')

# num = [10,20,30]
# for x in num:
    # if x ==20:
        # break
    # print(x)

# num = [10,20,30,40]
# for x in num:
    # print(x)
    # if x ==30:
        # contiue
    # print(x)

print('hello world one')

# num = [10,20,30,40]
# for x in num:
    # if x ==30:
        # contiue
    # print(x)

# num = [10,20,30,40]
# for x in num:
    # if x ==30:
        # break
    # print(x)

# num = [10,20,30,40]
# for x in num:
    # if x == 30:
        # continue
    # print(x)

# CONTINUE

# for x in range(6):
    # print(x)

for x in range(2,6):
    print(x)

for x in range(2,10,2):
    print(x)     #  then it give the value of     2 4 6 8   in different - different lines 
# incrementing by 2 


for x in range(2,10,3):
     print(x) #  then it give the value of     2 5 8   in different - different lines 
# incrementing by 3



for x in range(5):
    print(x)
else:
    print("finally the process is finished")


for x in range(5):
    if(x == 3): break 
    print(x)
else:
    print("finally the process is finished")  




# NESTED LOOPS

#  for matrix we use nested loops 
# if you want to create matrices , matrix are 2-D Spaces. 
#  if you want to create arrays , we use nested loops 
#  if you want to create algorithms , we use nested loops . 

arr1= [1,2]
arr2 = [5,6]
for x in arr1:
    for y in arr2:
        print(x,y)

# x = 1 , y = 5 , and y = 6 
# x = 2 , y = 5,  and  y = 6        
#  according to above method inner loop gets executed once for each iteration of the outer loop         





for x in [ 10 , 20 ,30 ]:
    pass
print('hello')
#  above method se hello ek bar aayega 


for x in [ 10 , 20 ,30 ]:
    pass
    print('hello')
#  above method se hello teen bar aa jayega ,alag alag line mein. 





for x in [ 10 , 20 ,30 ]:

    print('hello')

    #  above method se bhi  hello teen bar aa jayega ,alag alag line mein. 

    # we make star pattern using for loop ( NESTED LOOP).