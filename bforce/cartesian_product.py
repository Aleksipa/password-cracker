def cProduct(*args, repeat=1):

    def calculate(values, max):
        for first in max:   
            for current in values:
                yield first + (current,)

    result = iter(((),))             
    for level in tuple(map(tuple, args)) * repeat:
        result = calculate(level, result)
    return result