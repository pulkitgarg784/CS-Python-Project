from random import randrange
from os import system
player = {"name": "The Doctor", "armour_rating": 1, "weapon_name": "Sonic Screwdriver",
          "weapon_rating": 30, "hp": 100}
enemy_names = ["Cybermen", "Sontaran", "Weeping Angel", "Dalek"]

size = input("Enter map size (10 to 20): ")
playerPos = [0, 0]
enemies = {}
checkpoint = [randrange(0, int(size)), randrange(0, int(size))]
new_level = True
NearPlayer = False
level = 0

system("cls")


def attackEnemy(name):
    enemies[name][2] = enemies[name][2] - player["weapon_rating"]
    if enemies[name][2] > 0:
        enemies[name][2] = 0  # if health is less than 0, round it up to 0


def attackPlayer(name):
    player["hp"] = player["hp"] - \
        (enemies[name][3]/player["armour_rating"])


def spawn_enemy():
    for i in enemy_names:
        enemies[i] = [randrange(0, int(size)), randrange(0, int(size)), randrange(
            1, 100), randrange(1, 25)]  # [xpos, ypos, hp, attackEnemy]


def playerMovement():
    move = input("(W/A/S/D to move, F for Attack: )")
    if move == "w" and playerPos[0] > 0:
        playerPos[0] -= 1
    elif move == "a" and playerPos[1] > 0:
        playerPos[1] -= 1
    elif move == "s" and playerPos[0] < int(size) - 1:
        playerPos[0] += 1
    elif move == "d" and playerPos[1] < int(size) - 1:
        playerPos[1] += 1
    elif move == "e":
        if checkpoint[0] == playerPos[0] and checkpoint[1] == playerPos[1]:
            new_level = True
    elif move == "f":
        for i in enemies:
            if enemies[i][0] == playerPos[0] and enemies[i][1] == playerPos[1]:
                attackEnemy(i)
                attackPlayer(i)
            elif enemies[i][0] == playerPos[0] + 1 and enemies[i][1] == playerPos[1] + 1:
                attackEnemy(i)
            elif enemies[i][0] == playerPos[0] - 1 and enemies[i][1] == playerPos[1] + 1:
                attackEnemy(i)
            elif enemies[i][0] == playerPos[0] + 1 and enemies[i][1] == playerPos[1] - 1:
                attackEnemy(i)
            elif enemies[i][0] == playerPos[0] - 1 and enemies[i][1] == playerPos[1] - 1:
                attackEnemy(i)
            elif enemies[i][0] == playerPos[0] and enemies[i][1] == playerPos[1] + 1:
                attackEnemy(i)
            elif enemies[i][0] == playerPos[0] and enemies[i][1] == playerPos[1] - 1:
                attackEnemy(i)
            elif enemies[i][0] == playerPos[0] + 1 and enemies[i][1] == playerPos[1]:
                attackEnemy(i)
            elif enemies[i][0] == playerPos[0] - 1 and enemies[i][1] == playerPos[1]:
                attackEnemy(i)
    else:
        print("Invalid Move")


def render():
    system("cls")
    bg = '-'
    gen = [int(size)*[bg] for i in range(int(size))]
    gen[playerPos[0]][playerPos[1]] = '@'
    for i in enemies:
        if enemies[i][2] > 0:
            gen[enemies[i][0]][enemies[i][1]] = "M"
        else:
            gen[enemies[i][0]][enemies[i][1]] = "X"
    gen[checkpoint[0]][checkpoint[1]] = "D"
    print('\n'.join(' '.join(row) for row in gen))


def enemyAI():
    for i in enemies:
        if enemies[i][2] > 0:  # number of enemies is more than 0
            # enemies[i][0] is x coordinate of enemy, enemies[i][1] is y coordinate
            if enemies[i][0] == playerPos[0] and enemies[i][1] == playerPos[1]:
                attackEnemy(i)
                attackPlayer(i)
                NearPlayer = True
            elif enemies[i][0] == playerPos[0] + 1 and enemies[i][1] == playerPos[1] + 1:
                attackPlayer(i)
                NearPlayer = True
            elif enemies[i][0] == playerPos[0] - 1 and enemies[i][1] == playerPos[1] + 1:
                attackPlayer(i)
                NearPlayer = True
            elif enemies[i][0] == playerPos[0] + 1 and enemies[i][1] == playerPos[1] - 1:
                attackPlayer(i)
                NearPlayer = True
            elif enemies[i][0] == playerPos[0] - 1 and enemies[i][1] == playerPos[1] - 1:
                attackPlayer(i)
                NearPlayer = True
            elif enemies[i][0] == playerPos[0] and enemies[i][1] == playerPos[1] + 1:
                attackPlayer(i)
                NearPlayer = True
            elif enemies[i][0] == playerPos[0] and enemies[i][1] == playerPos[1] - 1:
                attackPlayer(i)
                NearPlayer = True
            elif enemies[i][0] == playerPos[0] + 1 and enemies[i][1] == playerPos[1]:
                attackPlayer(i)
                NearPlayer = True
            elif enemies[i][0] == playerPos[0] - 1 and enemies[i][1] == playerPos[1]:
                attackPlayer(i)
                NearPlayer = True
            else:
                NearPlayer = False
            if NearPlayer == False:
                c_move = randrange(1, 6)
                if c_move == 1 and enemies[i][0] < int(size) - 1:
                    enemies[i][0] += 1
                elif c_move == 2 and enemies[i][1] < int(size) - 1:
                    enemies[i][1] += 1
                elif c_move == 4 and enemies[i][0] > 0:
                    enemies[i][0] -= 1
                elif c_move == 5 and enemies[i][1] > 0:
                    enemies[i][1] -= 1


while player["hp"] > 0:  # player is alive
    if new_level == True:
        checkpoint = [randrange(0, int(size)), randrange(0, int(size))]
        enemies = {}
        spawn_enemy()
        render()
        level += 1
        new_level = False
    elif new_level == False:
        print("NAME:  " + player["name"])
        print("HEALTH:  " + str(player["hp"]))
        print("WEAPON:  " +
              player["weapon_name"] + ": " + str(player["weapon_rating"]) + " DMG")
        print("ARMOUR:  " +
              str(player["armour_rating"]))
        for i in enemies:
            print("ENEMY:  " + str(i) + "     " + "HP: " + str(enemies[i][2]) + "     " + "ATTACK: " +
                  str(enemies[i][3]))
        playerMovement()
        enemyAI()
        render()
        if checkpoint[0] == playerPos[0] and checkpoint[1] == playerPos[1]:
            new_level = True

print()
print()
print(" ----------------GAME OVER---------------- ")
print()
print("-----------You Reached Level: " + str(level) + " -----------")
