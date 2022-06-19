def operate(operator, *args):
    def add(x, *args):
        result = x
        for num in args:
            result += num
        return result

    def substract(x,*args):
        return x - (y for y in args)

    def multiply(x, *args):
        result = x
        for num in args:
            result *= num
        return result


    def devide(x, *args):
        result = x
        for num in args:
            result /= num

    if operator == '+':
        return add(*args)
    elif operator == '-':
        return substract(*args)
    elif operator == '*':
        return multiply(*args)
    elif operator == '/':
        return devide(*args)




