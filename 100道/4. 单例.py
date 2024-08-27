from functools import wraps


def singleton(class_):
    instances = {}

    @wraps(class_)
    def wrapper(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return wrapper

@singleton
class Singleton:
    def __init__(self, value):
        self.value = value


