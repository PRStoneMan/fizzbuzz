#pretty self explanatory
def checkDivides(number, divisor):
    if number % divisor == 0:
        return True
    else:
        return False

def fizzBuzz(number, conditions):
    output = []
    #I'm looping through all the conditions. Ex: in '3': 'fizz', the condition is '3'
    for condition in conditions:
        if (checkDivides(number, int(condition))):
                #if the condition, as an interger divides the number add it to the output 'output'
                output.append(conditions[condition])
    
    if len(output) != 0:
        #if the output isn't empty print it out as string
        return print(''.join(output))
        
    #if no conditions apply print the number
    return print(number)


#this exists so yu dont have to add the for loop. Not that usefull but still
def fancyFizzBuzz(numberRange, conditions):
    for number in numberRange:
        fizzBuzz(number, conditions)


# add here what conditions you'd like to have. If multiple conditions apply they'll both be printed
conditions = {
    '3': 'fizz',
    '5': 'buzz',
}

fancyFizzBuzz(range(1, 101), conditions)