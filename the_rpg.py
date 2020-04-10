import os
import time

def print_title(str):
    for letter in str:
        print(letter,end="")
        time.sleep(.000002)
    print()


def print_slow(str):
    for letter in str:
        print(letter,end="")
        time.sleep(.06)
    print()


def guard_enters(wall_value):
    print("Guard: So you are awake.")
    pass



def dungeon_start():
    time_count = 0
    wall = 0
    choices = {'1': "The door is made with strengthened steel. It's very durable.\n",
               '2': "These walls are pretty well made with very few cracks.\n",
               '3': "The copper utensil is cold and brittle. No food and probably not a weapon for you.\n",
               '4': "... Waiting... Waiting\n"}
    print("You wake up in a dungeon. Its a small brick-walled room.")
    time.sleep(1)
    print("You look across and you see :")
    time.sleep(1.8)
    print("The door made of iron bars")
    time.sleep(1.8)
    print("Almost no cracks in the wall")
    time.sleep(1.8)
    print("A copper utensil for eating food.")
    time.sleep(1.8)
    print("What do you do?")
    time.sleep(2)
    while time_count<4:
        print("What will you do ? (choose the number of your choice)")
        time.sleep(1)
        choice = input("1. Check the door\n2. Check the walls\n3. Look at the copper utensil\n4. Wait\n")
        time_count += 1
        if choice == 2:
            wall += 1
        if wall >= 2:
            choices['2'] = "These walls.... They are no ordinary walls. It's a part of hidden tunnel system. Your father had it made."
        print_slow(choices[choice])

    guard_enters(wall)



def init():
    home = os.path.expanduser('~')
    game_folder= "the_rpg_game"
    final_path = os.path.join(home, game_folder)

    # if not os.path.exists:
    #     os.makedirs(final_path)
    # save_file = "rpg_save_file.csv"
    #
    # with open(os.path.join(final_path, save_file), 'wb') as temp_file:
    #     temp_file.write()

def start():
    print("#"*200)
    print_title("         _______  _    _  ______ \n"            
          "         |__   __|| |  | ||  ____|\n"             
          "            | |   | |__| || |__  \n"            
          "            | |   |  __  ||  __| \n"             
          "            | |   | |  | || |____  \n"            
          "            |_|   |_|  |_||______|  \n"
          "     _____   _____     ____  __          __ _   _\n"
          "    / ____| |  __ \   / __ \ \ \        / /| \ | |\n"
          "   | |      | |__) | | |  | | \ \  /\  / / |  \| |\n"
          "   | |      |  _  /  | |  | |  \ \/  \/ /  | . ` |\n"
          "   | |____  | | \ \  | |__| |   \  /\  /   | |\  |\n"
          "    \_____| |_|  \_\  \____/     \/  \/    |_| \_|\n"
          "                    _   _  _____ \n"
          "             /\    | \ | ||  __ \ \n"
          "            /  \   |  \| || |  | | \n"
          "           / /\ \  | . ` || |  | | \n"
          "          / ____ \ | |\  || |__| | \n"
          "         /_/    \_\|_| \_||_____/ \n"
          "     ______  _                 __  __  ______\n"
          "    |  ____|| |         /\    |  \/  ||  ____| \n"
          "    | |__   | |        /  \   | \  / || |__ \n"
          "    |  __|  | |       / /\ \  | |\/| ||  __|\n"
          "    | |     | |____  / ____ \ | |  | || |____\n"
          "    |_|     |______|/_/    \_\|_|  |_||______|\n")
    print_title("#"*160)
    s1 = " Welcome to the Crown and Flame. An exicitng text-based RPG- Game "
    s2 = " In this game you will be assuming the role of a 17 year-old prince, "
    s3 = " in his own castle's dungeon after the attack of a neighbouring Kingdom. "
    s4 = " You were knocked unconscious and now wake up in the dungeon. "
    s5 = " Help guide the prince to his freedom! "
    s6 = " And reclaim your rightful throne. "
    print_title(s1.center(160, "#"))
    print_title(s2.center(160, "#"))
    print_title(s3.center(160, "#"))
    print_title(s4.center(160, "#"))
    print_title(s5.center(160, "#"))
    print_title(s6.center(160, "#"))
    print_title("#"*160)
    dungeon_start()


if __name__ == "__main__":
    init()
    start()