from time import sleep


def out(characters: str):
    sleep(1)
    print(characters, end='')


def paddle(water: str):
    if len(water) > 1:
        paddle(water[0:len(water)-1])
        paddle(water[1:len(water)])
    elif len(water) == 1:
        out(water)


if __name__ == "__main__":
    paddle("What")
