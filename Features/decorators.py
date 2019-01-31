def smart_divide(func):
    def inner(a, b):
        print("Dividing {} by {}".format(a, b))
        if b == 0:
            print("Attempt to divide by 0")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return a / b
