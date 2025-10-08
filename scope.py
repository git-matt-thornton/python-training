
name = "Dave"

count = 1


def another():
    colour = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal colour
        colour = "red"
        print(colour)
        print(name)

    greeting("Dave")


another()
