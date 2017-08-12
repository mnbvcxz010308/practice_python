#decorators tutorial

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print('Our wrapper executed before the {} function'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function
@decorator_function
def display():
    print('Display Function Ran !')
@decorator_function
def display_info(name,age):
    print('display_info ran with arguments {} and {}'.format(name,age))

display_info('John',25)
display()
