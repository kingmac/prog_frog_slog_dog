import random
enemy = 'Spider'
gender = True
merchant = "Josh"


def merchant_buy(merchant):
    gag = int(random.randint(1,10))
    mgag = int(random.randint(1,10))
    print("You rolled a", gag)
    print("The" + merchant + "rolled a", mgag)
    input()
    if gag > mgag:
        print("You lost...\nYou bet your life")
        store(h)
    elif gag < mgag:
        print("You won allot of gold main!")
        gold = 100
        store(h)


def fight_enemy(enemy):
    fdmg1 = int(random.randint(1,7))
    edmg1 = int(random.randint(1,6))
    print("You hit a", fdmg1)
    print("The " + enemy + " hits a", edmg1) # <== Changed
    input()
    if edmg1 > fdmg1:
        print("You died")
    elif edmg1 < fdmg1:
        print("You killed the " + enemy) # <== Changed
    else:
        print("You didnt kill the " + enemy + " but you managed to escape") # <=== Changed

def intro_1():
    print("\nYou're a man with a mission or girl idc tbh\n wait hold you you choose ok?")
    gender = input("\n[What is gender]\n")
    print("\nYou're a {} c now i care ^.^".format(gender))
    input()
    print("\nGood luck {}".format(gender))   
if gender == True:
    fight_enemy(enemy)
else:
    intro_1()
#ask bridger to help with gender - true so it will call on fight function after answers the gender questoin.




