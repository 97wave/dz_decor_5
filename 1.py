from datetime import datetime

def logger(function):
    def new_function(x):
        result = function(x)
        log_string = f"{datetime.today()} {function.__name__}({x}) = {result}"
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(log_string + '\n')
        return result
    return new_function


@logger
def square_x(x):
    return x*x

print(square_x(int(input())))