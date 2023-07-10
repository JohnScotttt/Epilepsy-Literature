import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("欢迎来到掷骰子游戏！")
    while True:
        input_str = input("按下 Enter 键掷骰子，输入 'q' 退出游戏：")
        if input_str.lower() == 'q':
            break
        else:
            dice_value = roll_dice()
            print("你掷得了：", dice_value)

if __name__ == "__main__":
    main()
