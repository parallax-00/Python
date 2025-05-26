import time
def timer(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args,**kwargs)
        end_time= time.time()
        print(f"Time taken by the function: {function.__name__}, to run is: {end_time - start_time}")
        return result
    return wrapper
         
@timer
def example_function(m):
    time.sleep(m)
    
example_function(2)