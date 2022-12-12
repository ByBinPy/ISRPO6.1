def calc(sign,a,b):
    for i in range(len(str(a))):
        if (str(a)[i] not in "0123456789" and i > 0):
            return None
        if (str(a)[i] == "-" and i != 0):
            return None
    for i in range(len(str(b))):
        if (str(b)[i] not in "0123456789" and i > 0):
            return None
        if (str(b)[i] == "-" and i != 0):
            return None   
    try:
        if sign == '+':
            return a+b
        if sign == '-':
            return a-b
        if sign == '*':
            return a*b
        if sign == '/':
            return a/b
    except ZeroDivisionError:
        return None
    except ValueError:
        return None
    except TypeError:
        return None
        
