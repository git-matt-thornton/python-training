
from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the range"


def randomfunfact():
    funfacts = [
        "Fun fact 1",
        "Fun fact 2",
        "Fun fact 3",
        "Fun fact 4"
    ]

    index = choice("0123")

    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfact()
