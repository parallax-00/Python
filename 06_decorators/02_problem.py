def debug(function):
    def wrapper(*args,**kwargs):
        return function(*args,**kwargs)        

    return wrapper



@debug
def greeting(name, greet="Hello!"):
    print(f"{greet}, {name}")

greeting("Parallax") 