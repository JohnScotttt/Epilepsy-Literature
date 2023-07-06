import random
from faker import Faker
import time


def drunk(inaudible="fuck you!", language="zh_CN"):
    fk = Faker(locale=language)
    if language == "en_US":
        for i in range(1, len(inaudible)):
            time.sleep(random.random())
            if i % (int(str(int(time.time()*1000000))[-1:-2:-1])+1) == 0:
                print(","+fk.word(), end=' ')
            else:
                print(fk.word(), end=' ')
        else:
            print(".")
    else:
        for i in range(1, len(inaudible)):
            time.sleep(random.random())
            if i % (int(str(int(time.time()*1000000))[-1:-2:-1])+1) == 0:
                print(","+fk.word(), end='')
            else:
                print(fk.word(), end='')
        else:
            print(".")


if __name__ == "__main__":
    drunk("草泥马，滚呐！")
