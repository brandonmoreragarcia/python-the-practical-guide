

def normal_function(*args, param_function):
    print('args', args)
    print(map(param_function, args))


normal_function(5,6,7,8,9,10, param_function = lambda x: x + 1)