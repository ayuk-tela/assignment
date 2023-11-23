import math
for x in range(-3, 3):
    try:
        result = math.sin(x) / x
        print('the value is', result)
    except ZeroDivisionError:
        print('cannot calculate')
    except ValueError:
        print('cannot calculate sin(x) as it is underdefined')