def outer():
    x = 6
    def inner():
        return x
    
    return inner




s = outer()


print(s())



