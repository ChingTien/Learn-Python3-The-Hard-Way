from sys import exit

#feed the baby
def baby_food():
    print("what will you feed your baby?")
    food = input("Milk or Cookie?  ")

    if "milk" or "Milk" in food:
        print("the baby is happy, you saved the day!")
        print("嬰兒今天喝仙草牛奶，超可愛")
        print("你贏了")
        exit(0)
    elif "cookie" or "Cookie" in food:
        print("嬰兒不能吃餅乾！餅乾是娃子的啦！！！")
        print("再見了")
        exit(0)
    else:
        print("enter again")
        baby_food()

#baby start crying
def start():
    print("the baby started crying!!! What should you do?")
    print("Feed the baby \t Comfort the baby \t Ignore the baby")

    choice = input(">")
    
    if "feed" or "Feed" in choice:
        baby_food()
    elif "comfort" or "Comfort" in choice:
        print("嬰兒有人安慰，很高興")
        print("你贏了！")
        exit(0)
    elif "ignore" or "Ignore"in choice:
        print("嬰兒酸掉了")
        print("再見了")
        exit(0)
    else:
        print("please enter again")
        start()


start()