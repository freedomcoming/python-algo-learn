def outer(f):
    print("装饰器outer")

    def inner(*args, **kwargs):
        print("装饰器inner")
        return f(*args, **kwargs)

    return inner


@outer
def func(x):
    print("func", x)


if __name__ == "__main__":
    func(1)
