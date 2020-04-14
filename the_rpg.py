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
    prCyan("Guard: HEY.... Looks like you are awake..")
    time.sleep(0.8)
    prCyan("Guard: Doesn't this look all familiar? It's your castle's dungeon after all.")
    time.sleep(1)
    prYellow("You: Where is Marx...? ")
    time.sleep(1)
    prCyan("Guard: Show Respect.. It's Lord Marx.")
    time.sleep(0.6)
    prCyan("Guard: His Majesty is out reclaiming Dominots for himself.")
    time.sleep(0.4)
    prYellow("You: That is my Kingdom.!!!1")
    time.sleep(0.5)
    prCyan("Guard: Not anymore. Well, rot in here for the rest of your life. Hehehe")
    print_slow(".........")
    print_slow("The guard leaves.")
    prYellow("You: I need to escape from here and let Chiron know of all this.\n\n\n")
    time.sleep(0.4)
    prYellow("You: Looks like a small opening at the top right corner of the ceiling, ")
    time.sleep(0.4) #find a way to print colored text slowly
    prYellow(" I need to somehow reach there to have a idea of where I am.")
    time.sleep(0.4)
    print_slow("You see a prick on the wall\nAnd you somehow have to get a hold of it to take a look\nfrom the hole.")
    #haany, make a choice option for the user to get a hold of this prick or something that user can take a look outside
    #user will encounter a old wise snake over there who is hungry from ages, and if he helps the snake get some #
    #food by snake game, the snake will help him get to somewhere out
    #i will be adding that snake game soon, u just make the option thing and also tell me that how can we link that
    #snake game to this rpg
    pass



def dungeon_start():
    time_count = 0
    wall = 0
    choices = {'1': "The door is made with strengthened steel. It's very durable.\n",
               '2': "These walls are pretty well made with very few cracks.\n",
               '3': "The copper utensil is cold and brittle. No food and probably not a weapon for you.\n",
               '4': "... Waiting... Waiting\n",
               '5': "You are no one to be here. You COWARD!"
               }
    prLightPurple("You wake up in a dungeon. Its a small brick-walled room.")
    time.sleep(1)
    prLightPurple("You look across and you see :")
    time.sleep(1.6)
    prLightPurple("The door made of iron bars")
    time.sleep(1.6)
    prLightPurple("Almost no cracks in the wall")
    time.sleep(1.6)
    prLightPurple("A copper utensil for eating food.")
    time.sleep(1.6)
    prLightPurple("What do you do?")
    time.sleep(2)
    while time_count<4:
        prRed("What will you do ? (choose the number of your choice)")
        time.sleep(1)
        choice = input("1. Check the door\n2. Check the walls\n3. Look at the copper utensil\n4. Wait\n")
        time_count += 1
        if choice == 2:
            wall += 1
        if wall >= 2:
            choices['2'] = "These walls.... They are no ordinary walls. It's a part of hidden tunnel system. Your father had it made."
        print_slow(choices[choice])
        # if choice > 4:
        #     prRed("You are no one to be here. You COWARD!")
    guard_enters(wall)

# colored text and background.
#use these pr functions for print statements
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


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