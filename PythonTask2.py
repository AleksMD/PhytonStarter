# The main purpose of this programm is to output all numbers multiple 5 in a range of two user-defined numbers.

x = int(input('Number 1: '))
x1 = int(input('Number 2: '))

while x <= x1:
    z = x % 5
    if z == 0:
            print(x)
    x = x + 1    
    

    
