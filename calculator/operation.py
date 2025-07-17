def operation(x,y,z):
    operations = ['+','-','*','/']
    if z in operations:
        if z == '+':
            return x + y
        elif z == '-':
            return x - y
        elif z == '*':
            return x * y
        elif z == '/':
            return x / y
        return None
    else:
        raise Exception

