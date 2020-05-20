###two decorators, my_logger and\ my_timer
from functools import wraps
#to solve the name confusements
#adding logging functionality to every funnction we want to
def my_logger(original_function):
    import logging
    logging.basicConfig(filename='.\logs\{}.log'.format("_"+original_function.__name__), level=logging.INFO)

    @wraps(original_function)
    def wrapper_func(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper_func

#timing how much each function runs for
def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper_func(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in {} seconds'.format(original_function.__name__, t2))
        return result
    return wrapper_func


####################main code#######################
import time

@my_logger
@my_timer
def greetings(first_name, last_name):
    time.sleep(2)
    print("Hi! {}{}\n Hope you are doing well. Please Proceed... ")

#greetings = my_logger( my_timer(greetings) )


greetings(first_name ="Mithilesh", last_name="Singh")


