def my_decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator received arguments: {arg1}, {arg2}")
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@my_decorator_with_args("arg1_value", "arg2_value")
def my_function():
    print("Inside the function")


my_function()
