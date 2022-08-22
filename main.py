from os import system, name
import operator

operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

def inputNumbers(i):
    global firstNumber, secondNumber
    if i == 1:
        try: firstNumber = float(input("First number? "))
        except:
            print("Invalid input.")
            inputNumbers(1)
    if i == 2:
        try: secondNumber = float(input("Second number? "))
        except:
            print("Invalid input.")
            inputNumbers(2)

def inputOperation():
    global selectedOperator
    selectedOperator = input("Operation? ")
    if not selectedOperator in operations:
        print("Invalid input. Use +, -, *, or /")
        inputOperation()

def clearScreen():
    if name == 'nt': system('cls')
    else: system('clear')

def rmZeros(i): return ('%f' % i).rstrip('0').rstrip('.')

def math():
    clearScreen()

    inputNumbers(1)
    inputOperation()
    inputNumbers(2)

    print("%s %s %s = %s" % (rmZeros(firstNumber), selectedOperator, rmZeros(secondNumber), rmZeros(operations[selectedOperator](firstNumber, secondNumber))))

    if input("Continue? (Y/N) ").lower() == 'y':
        math()
math()
