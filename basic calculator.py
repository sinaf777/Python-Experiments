while True:
    print('           Welcome         ')
    print('----------------------------')
    print('1, Addition')
    print('2, Subtraction')
    print('3, Multiplication')
    print('4, Division')
    try:
        value = int(input('Choose an option: '))
        if value == 1:
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
            print('Your result is: ', num1 + num2)
        elif value == 2:
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
            print('Your result is: ', num1 - num2)
        elif value == 3:
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
            print('Your result is: ', num1 * num2)
        elif value == 4:
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
            if num2 == 0:
               print('0 can not be divisible!!!')
            else:
               print('Your result is: ', num1 / num2)
        else:
            print('Wrong input!')
            print('Please choose between (1-4)')
    except ValueError:
        print('Invalid input choose between (1 - 5)')
print()
