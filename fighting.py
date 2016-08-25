import sys, random, time


enemies = [
	['Spider', 1, 7],
    ['Skeleton', 4, 10],
    ['Goblin', 6, 10]
]

weapons = [
	['Sword', 1, 7],
	['Axe', 3, 12],
	['Dildo', 5, 10]
]

wpn = 0

def main():
	global wpn

	fgn = 0;

	while (True):
		win = fight_enemey(enemies[fgn])

		if win == True:
			print("\nYou win!")
			fgn += 1
			wpn += 1
			print("\nYou earned a new weapon", weapons[wpn][0])

			if fgn >= len(enemies):
				print ("\nYou beat them all!\n")
				break

		else:
			print("\nYou lost")
			break



def fight_enemey(enemy):
	input("\nPress enter to fight!\n")

	fgt = random.randrange(weapons[wpn][1], weapons[wpn][2])
	fge = random.randrange(enemy[1], enemy[2])

	if fgt > fge:
		print ("You hit a", fgt,)
		return True
	else:
		print("The " + enemy[0] + " Hits a", fge)
		return False






#Stay to the bottom of program
main()
