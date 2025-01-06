while True:
    print('-----------------------------------------------------')
    print('         Pythagoras Theorem Equation Solver         ')
    print('-----------------------------------------------------')
    print('A² + B² = C² Pythagoras Formula')
    print('1, Find A')
    print('2, Find B')
    print('3, Find C')
    print('4, Exit')
    try:
        value = int(input('Choose an oppration: '))
        if value == 1:
            print('      To find the value of A')
            print('----------------------------------')
            b = float(input('Enter the value of B: '))
            c = float(input('Enter the value of C: '))
            sol = (c**(2)- b**(2))**(1/2)
            print('----------------------------------')
            print('Solution A =',sol)
        elif value == 2:
            print('      To find the value of B ')
            print('----------------------------------')
            c = float(input('Enter the value of C: '))
            a = float(input('Enter the value of A: '))
            sol = (c**(2)-a**(2))**(1/2)
            print('----------------------------------')
            print('Solution B = ',sol)
        elif value == 3:
            print('      To find the value of C ')
            print('----------------------------------')
            a = float(input('Enter the value of A: '))
            b = float(input('Enter the value of B: '))
            sol = (a**(2)+b**(2))**(1/2)
            print('Solution C = ',sol) 
        else:
            print('Exiting.....')
            break
    except ValueError:
        print('Wrong input!!')
        print('Enter between 1-4')
