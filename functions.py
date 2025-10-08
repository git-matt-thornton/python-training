
def hello_world():
    print("\nHello World!\n")


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


def multiple_items(*args):
    print(args)
    print(type(args))


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


hello_world()

total = sum(7, 2)
print(total)

mult_named_items(first="Dave", last="Gray")
