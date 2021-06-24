from datetime import datetime

def logger(log_path):
    def _logger(function):
        def new_function(*args, **kwargs):
            result = function(*args, **kwargs)
            log_string = f"{datetime.today()} {function.__name__}(args={args}, kwargs={kwargs}) = {result}"
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(log_string + '\n')
            return result
        return new_function
    return _logger