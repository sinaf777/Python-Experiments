# Dollar-to-ETB-converter

print("Dollar to ETB converter using python")
dollar = input("enter amount in $: ")
dollar = float(dollar)
birr = dollar * 140
print(birr, "Birr")

# Odd Even checker
number=int(input("Enter number:"))
if number %2 == 0:
    print("Even")
else:
    print("Odd")
# Square using for loop
n = 8
for i in range (n):
    for j in range (n):
        print('*', end = '  ')
    print()
# Increasing Left side triangle using for loop
n = 8
for i in range (n):
    for j in range(1+i):
        print('*', end = ' ')
    print()
# Decreasing Left side triangle using for loop
n = 8
for i in range (n):
    for j in range (i,n):
        print('*', end =' ')
    print()
# Increasing Right side triangle using for loop
n = 8
for i in range (n):
    for j in range (i,n):
        print(' ', end = ' ')
    for j in range (1+i):
        print('*', end = ' ')
    print()
# Decreasing Right side triangle using for loop
n = 8
for i in range (n):
    for j in range (1+i):
        print(' ', end =' ')
    for j in range (i,n):
        print('*', end = ' ')
    print()
# Pyramid
n = 8
for i in range (n):
    for j in range (n-i-1):
        print(' ', end = ' ')
    for j in range (2*i+1):
        print('*', end = ' ')
    print()    
