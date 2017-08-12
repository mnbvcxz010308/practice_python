from functools import wraps
def my_logging(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__),level=logging.INFO)

    @wraps(original_function)
    def wrapper_function(*args,**kwargs):
        logging.info('{} function ran with args: {} and kwargs: {}'.format(original_function.__name__,args,kwargs))
        return original_function(*args,**kwargs)
    return wrapper_function

@my_logging
def display_info(name,age):
    print('display_info function ran with {} and {} arguments'.format(name,age))

display_info('John',25)
print(display_info.__name__)
