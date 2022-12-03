
import random

num = random.random()   #  it generates a random float number between 0 to 1 . 
print(num)




import random

# num = random.random()   
num = random.randint(0,10)
print(num)





# create a list of 5 random intergers.
import random
randomlist = []

for i in range(0,5):
    num = random.randint(1,20)
    randomlist.append(num)
print (randomlist)    



import random
randomlist = random.sample(range(1,20), 5)
print(randomlist)







