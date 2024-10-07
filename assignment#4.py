

def normal_function(*args, fn):
    for arg in args:
        print(fn(arg))


normal_function(5,6,7,8,9,10, fn = lambda x: x + 1)