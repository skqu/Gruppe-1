
## Calculate 2 numbers 
def calc(float_num1, str_operator, float_num2):
    match str_operator:
        case "+":
            float_result = float_num1 + float_num2
        case "-":
            float_result = float_num1 - float_num2
        case "*":
            float_result = float_num1 * float_num2
        case "/":
            try:
                float_result = float_num1 / float_num2
            except ZeroDivisionError:
                print("0 is not divisible")
                exit()

    print("Result: ", float_num1 , str_operator, float_num2, " = ", float_result) 


def userInput(float_num1 = 0): 
    try:
        ## If there is no 1. nr display input for 1. nr
        if(not float_num1):
            float_num1 = float(input("1. num: "))

        str_operator = input("Choose operator (+ - * /): ")
        array_operator = ["+", "-", "*", "/"]
        
        ##If operater is invalid run userInput again with the first nr as a paramater 
        if(not str_operator in array_operator):
            print("Unidentified operator")
            userInput(float_num1)
        
        float_num2 = float(input("2. num: "))

        calc(float_num1, str_operator, float_num2 )

    except ValueError:
        print("Needs to be a number")

userInput()


