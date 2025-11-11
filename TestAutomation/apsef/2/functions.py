#Function name
#     Input parameter(argument)
print('hi')

#When using print, we are doing a function call 
#since we are calling the function print
print('hello', 'world')

#Reasigning a new name to an existing function 
other_print = print
other_print('Print with a new name')

#Creating a function from scratch
def do_math(num1,num2=7): #asigning a default value to the function by adding '='
    #parameters
    result = num1 * num2
    result += 10
    result /= 1.5
    result -= num1
    return result

print(do_math(5))
print(do_math(8, 10))

#Importing operators library
import operator
print(operator.add(2,1))
print(operator.not_(True))

def other_function(arg1, arg2='a', arg3=None, arg4=True, arg5='hello'):
    pass

other_function(1, arg4=False)