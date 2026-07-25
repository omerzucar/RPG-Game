import random
from random import choice
from enemies import enemies


player = {"Name": "Tiger", "Health": 100, "Power": 10, "Inventory": []}


def create_character():
    global player
    character_name = ""
    while character_name == "":
        character_name = str(input("What do you want to give a name on the character?: "))
        if character_name == "":
            print("You did not write a name.")
    player["Name"] = character_name

def add_item():
    global player
    avaible_items = ["sword", "gun", "laser eyes"]
    item_name = str(input("What do you want to take an items?: 'Sword', 'Gun', 'Laser Eyes' ")).lower()

    while item_name not in avaible_items:
        print("You did not write a valid item. Please select an item.")
        item_name = str(input("What do you want to take an item?: 'Sword', 'Gun', 'Laser Eyes' ")).lower()

    player["Inventory"].append(item_name)
    print(f"{item_name} added to inventory.")


def use_item():
    global player
    item_name = str(input("What item do you want to use?: ")).lower()

    if item_name in player["Inventory"]:
        player["Inventory"].remove(item_name)
        player["Health"] += 10
        print(f"{item_name} used. Health increased.")
    else:
        print("You don't have that item in your inventory.")


def show_inventory():
    if player["Inventory"] == []:
        print("You don't have any items in your inventory.")
    else:
        print(f"{player['Inventory']}")

def create_enemy():
    enemy1 = random.choice(enemies).copy()
    enemy2 = random.choice(enemies).copy()
    while enemy2 == enemy1:
        enemy2 = random.choice(enemies).copy()
    return enemy1, enemy2

def fight(enemy1, enemy2):
    global player

    while player["Health"] > 0 and (enemy1["Health"] > 0 or enemy2["Health"] > 0):
        if enemy1["Health"] > 0:
            enemy1["Health"] -= player["Power"]
            print(f"You attacked {enemy1['Name']}. {enemy1['Name']}'s health: {enemy1['Health']}")
        elif enemy2["Health"] > 0:
            enemy2["Health"] -= player["Power"]
            print(f"You attacked {enemy2['Name']}. {enemy2['Name']}'s health: {enemy2['Health']}")
        if enemy1["Health"] > 0:
            player["Health"] -= enemy1["Power"]
            print(f"{enemy1['Name']} attacked you. Your health: {player['Health']}")
        if enemy2["Health"] > 0:
            player["Health"] -= enemy2["Power"]
            print(f"{enemy2['Name']} attacked you. Your health: {player['Health']}")
    if player["Health"] <= 0:
        print("You lost the fight.")
        return False
    else:
        print("You defeated both enemies!")
        return True


def chapter_1():
    print("You wake up at the edge of a dark forest. Two paths lie ahead:")
    print("1) Enter the forest")
    print("2) Walk to the village")

    try:
        choice = int(input("Your choice (1/2): "))
    except ValueError:
        print("Invalid input, please type 1 or 2.")
        return chapter_1()

    if choice == 1:
        print("You step into the forest...")
        chapter_2()
    elif choice == 2:
        print("You walk toward the village...")
        chapter_3()
    else:
        print("Invalid choice, try again.")
        chapter_1()


def chapter_2():
    print("The forest is dark and quiet. Suddenly you hear a rustling noise nearby.")
    print("1) Investigate the noise")
    print("2) Keep walking, ignore it")

    try:
        choice = int(input("Your choice (1/2): "))
    except ValueError:
        print("Invalid input, please type 1 or 2.")
        return chapter_2()

    if choice == 1:
        print("You move toward the noise and a creature jumps out at you!")
        enemy1, enemy2 = create_enemy()
        won = fight(enemy1, enemy2)
        if won:
            chapter_4()
        else:
            summary_of_game(False)
    elif choice == 2:
        print("You keep walking and reach a narrow bridge.")
        chapter_4()
    else:
        print("Invalid choice, try again.")
        chapter_2()


def chapter_3():
    print("You arrive at a small village. People are going about their day.")
    print("1) Talk to a merchant")
    print("2) Rest at the inn")

    try:
        choice = int(input("Your choice (1/2): "))
    except ValueError:
        print("Invalid input, please type 1 or 2.")
        return chapter_3()

    if choice == 1:
        print("The merchant offers you an item.")
        add_item()
        chapter_4()
    elif choice == 2:
        print("You rest at the inn and recover some health.")
        player["Health"] += 20
        chapter_4()
    else:
        print("Invalid choice, try again.")
        chapter_3()


def chapter_4():
    print("Both paths lead you to an old stone bridge guarded by enemies.")
    enemy1, enemy2 = create_enemy()
    won = fight(enemy1, enemy2)
    if won:
        chapter_5()
    else:
        summary_of_game(False)


def chapter_5():
    print("Beyond the bridge, you find a wounded traveler who gives you advice.")
    print("1) Use an item to help them")
    print("2) Continue on your journey")

    try:
        choice = int(input("Your choice (1/2): "))
    except ValueError:
        print("Invalid input, please type 1 or 2.")
        return chapter_5()

    if choice == 1:
        use_item()
        chapter_6()
    elif choice == 2:
        print("You continue walking, saving your resources.")
        chapter_6()
    else:
        print("Invalid choice, try again.")
        chapter_5()


def chapter_6():
    print("You reach the final gate. A powerful enemy blocks your way.")
    enemy1, enemy2 = create_enemy()
    won = fight(enemy1, enemy2)
    if won:
        summary_of_game(True)
    else:
        summary_of_game(False)


def chapter_ending_win():
    print(f"Congratulations, {player['Name']}! You have defeated your enemies and completed the journey!")
    summary_of_game(True)


def chapter_ending_lose():
    print(f"You have fallen, {player['Name']}. Your journey ends here.")
    summary_of_game(False)

def summary_of_game(won):
    print("Game Summary")
    print(f"Player Name: {player['Name']}")
    print(f"Remaining Health: {player['Health']}")
    print(f"Items in Inventory: {len(player['Inventory'])}")
    if won:
        print("Result: You won the game!")
    else:
        print("Result: You lost the game.")

def start_game():
    print("Welcome to the game! I hope you will enjoy it.")
    create_character()
    chapter_1()

if __name__ == "__main__":
    start_game()