
try:
    num1 = int(input('Enter the first number'))
    num2 = int(input('Enter the second number'))
except Exception as e:
    print('please enter valid data')
    print(e)
    exit(0)



n = input("enter the operation + - * /")





match n:
    case '+':
        print(f'the answer of addition is{num1 + num2}')

    case '-':
        print(f'the answer of addition is{num1 - num2}')

    case '*':
        print(f'the answer of addition is{num1 * num2}')

    case '/':

        if num2 == 0:
            print('cannot divide by zero')
        else:    
            print(f'the answer of addition is{num1 + num2}')    

    case _:
        print('not a valid operator!')


  
