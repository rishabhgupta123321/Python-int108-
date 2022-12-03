# x = int(input("x: "))
# y = int(input("y: "))
# a = bin(x).replace("0b","")
# b = oct(y).replace("0o","")
# print(f"{a},{b}")










# qn no 17 sir, for n=5,sum of
#  2+22+222+2222+22222=,expected 
#  output=24690

#  ABOVE QUESTION KA CODE BELOW HAI-----

n = 5  
start = 2

sequence = 0 

for x in range(0, n):
    sequence = sequence + start

    start = start * 10 + 2
print(sequence)



n = 5  
start = 2

sequence = 0 

for x in range(0, n):
    sequence = sequence + start
    print('sequence', sequence)
    start = start * 10 + 2
    print('start', start)
print('Sum of the series is ', sequence)






