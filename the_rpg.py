from RPG_IO import *
import time
import os


def the_escape():
    bee = 0
    prSloYellow("You: .... ... Now what do I do?.......")
    time.sleep(1.2)
    prSloYellow("You: ... Wait a moment! ")
    time.sleep(0.4)
    prSloYellow("You: Looks like a small opening at the right corner of the ceiling.. ")
    time.sleep(0.7)
    prSloYellow("You: But its not like I can dig my way out of here...")
    time.sleep(0.7)
    print_slow("What will you do?")
    while bee < 2:
        ans = putin("1. Check out the hole again...\n2. Do Nothing.\n3. Try yelling at the guards\n", "int")
        if ans == "1":
            print_slow("The hole is not big enough for even your arm....")
            time.sleep(0.5)
            break
        else:
            bee += 1
            if ans == "2":
                print_real_slow("....")
            elif ans == "3":
                prSloYellow("You: IS ANYONE THERE!!?????")
                time.sleep(0.4)
                print_slow(".....Looks like no guards are around....")
    print_slow("...BBBZZZZZZ..... BBBZZZZZZZZZZ...... ")
    print_slow(".. A bee comes in thorugh the hole.")
    prSloYellow("You: Great! Just what I needed.")
    print_real_slow("...")
    prSloYellow("You: .... If a bee can come in, that means I'm not in the under-ground dungeon.")
    print_slow("You get up and have a close look at the hole. ")
    print_slow("You notice light coming thorugh it.")
    print_slow("Of course. If light is coming through, then you can break free.")
    print("You try clawing around the hole. Your hands end up bloodied.")
    time.sleep(1.3)
    print("But you manage to make the hole big enough for you to pass through.")
    time.sleep(1)



#############################################################################################################
########################## THE COMMENT SECTION #####################################
##########################################################################################################
# We will keep this area just for commenting and leaving notes to each other about the changes made.
# Update/Delete all of this when you've read it, but not that above 'comment section' tag.

# I was thinking of making a choice here of taking the bronze plate along or not.
# But the thing is, if we do that, then we will have to maintain an inventory as well
# What do you say? Limited Inventory. The player will not be able to check it all the time.
# Coz that would just make stuff problematic for us.
# Just make use of things in it on special occasions. Special areas in game will unlock special scenes,
# if you have certain items at that point in your inventory
# Do we go ahead with it?

# As for secret passage, we will try not to think about it much.. its just a shortcut, to almost direct exit
# out of castle. But both secret passage and the_escape will make MC reach a common point.
# Albeit, secret_passage will be shorter

# I also added a new method called putin.. Be sure to check out that method in RPG_IO file..
# We will be using this for taking in user input.

def secret_passage():
    prSloYellow("You: Looks like everyone is gone.")
    prSloYellow("You:.. Now, about that hidden passage.")
    prSloYellow("You: Chiron did tell me it almost connects the entire castle.")
    prSloYellow("This place is certainly not the dungeons. ")
    prSloYellow("The passage was never connected to them.")
    prSloYellow("I don't care either way. I have to get out.")


def guard_enters(wall_value):
    prSloCyan("Guard: HEY.... Looks like you are awake..")
    prSloCyan("Guard: Doesn't this look all familiar? It's your castle's dungeon after all.")
    prSloYellow("You: Where is Marx...? ")
    prSloCyan("Guard: How DARE YOU!!???! ... It's Lord Marx.")
    prSloCyan("Guard: His Majesty is out reclaiming Dominots for himself.")
    prSloYellow("You: This is MY Kingdom.!!!!")
    prSloCyan("Guard: Not anymore. Well, rot in here for the rest of your life. Hehehe")
    print_slow(".........")
    print_slow("The guard leaves.")
    prSloYellow("You: I need to escape from here and let Chiron know of all this.\n\n\n")
    if wall_value >= 2:
        secret_passage()
    else:
        the_escape()


def dungeon_start():
    time.sleep(2)
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
        prRed("(choose the number of your choice)")
        time.sleep(1)
        choice = putin("1. Check the door\n2. Check the walls\n3. Look at the copper utensil\n4. Wait\n", "int")

        time_count += 1
        if choice == "2":
            wall += 1
        if wall >= 2:
            choices['2'] = "These walls.... They are no ordinary walls. It's a part of hidden tunnel system that Chiron told you."
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
    print("#"*150)
    print_logo("          _______  _    _  ______ \n"            
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
    print_logo("#"*150)
    time.sleep(1.5)
    s1 = " Welcome to the Crown and Flame. An exicitng text-based RPG- Game "
    s2 = " In this game you will be assuming the role of a 17 year-old prince, "
    s3 = " locked in his own castle's dungeon after the attack of a neighbouring Kingdom. "
    s4 = " You were knocked unconscious and now wake up in the dungeon. "
    s5 = " Help guide the prince to his freedom! "
    s6 = " And reclaim your rightful throne. "
    print_title(s1.center(150, "#"))
    print_title(s2.center(150, "#"))
    print_title(s3.center(150, "#"))
    print_title(s4.center(150, "#"))
    print_title(s5.center(150, "#"))
    print_title(s6.center(150, "#"))
    print_title("#"*150)


if __name__ == "__main__":
    init()
    start()
    dungeon_start()