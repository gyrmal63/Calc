import operator

operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

firstNumber = float
selectedOperator = str
secondNumber = float

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
        print("Invalid input.")
        inputOperation()

def rmZeros(i): return ('%f' % i).rstrip('0').rstrip('.')

inputNumbers(1)
inputOperation()
inputNumbers(2)

print("%s %s %s = %s" % (rmZeros(firstNumber), selectedOperator, rmZeros(secondNumber), rmZeros(operations[selectedOperator](firstNumber, secondNumber))))