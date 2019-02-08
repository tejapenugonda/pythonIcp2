x = int(input("Enter first number"))
y = int(input("Enter 2nd number"))
print('Addition: x + y = ',x+y)
print('Subtraction: x - y = ',x-y)
print('Multiplication: x * y =',x*y)
print('Division: x / y =',x/y)
print('Integer Division: x // y =', x//y)
print('Power function: x * y =', x*y)
print('Greater: x > y  is', x>y)
print('Lesser: x < y  is', x<y)
print('Equal: x == y is', x==y)
print('Not Equal: x != y is', x!=y)
print('Greater or Equal: x >= y is', x>=y)
print('Lesser or Equal: x <= y is', x<=y)



a = (input("Enter Firstname"))
b = (input("Enter lastname"))
print (a[::-1]+" "+b[::-1])



a = input("Enter a sentence")
num_count = 0
char_count = 0
space_count = 0
for i in a:
    if i.isdigit():
        num_count=num_count+1
    elif i.isalpha():
        char_count=char_count+1
    elif i.isspace():
        space_count=space_count+1
print ("Number of numbers " + str(num_count))
print ("Number of charectors "+ str(char_count))
print ("Number of spaces "+ str(space_count))