import time

def print_logo(str):
    for letter in str:
        print(letter, end="")
        time.sleep(.00577)
    print()

def print_title(str):
    for letter in str:
        print(letter, end="")
        time.sleep(.02)
    print()

def print_real_slow(str):
    for letter in str:
        print(letter, end="")
        time.sleep(.6)
    print()

def print_slow(str):
    for letter in str:
        print(letter, end="")
        time.sleep(.06)
    print()


def putin(string_msg, typ, alternative_text="Enter proper choice"):
    """
    The function makes sure the user inputs the proper value and persists until the user gives a proper value
    :param string_msg: Storing the input message prompt.
    :param typ: What type of input is to be expected from the user. Either "int" or "str".
    :param alternative_text: The message to be displayed when wrong input is given.
    :return:
    """
    ans = input(string_msg)
    if typ == 'int':
        while True:
            if not ans.isdigit():
                print_slow(alternative_text)
                ans = int(string_msg)
            else:
                break
        return int(ans)
    elif typ == 'str':
        while True:
            if not ans.isalpha():
                print_slow(alternative_text)
                ans = input(string_msg)
            else:
                break
        return ans


# functions for colored text output - regular fashion
def prRed(stmt): print("\033[91m {}\033[00m".format(stmt))
def prGreen(stmt): print("\033[92m {}\033[00m".format(stmt))
def prYellow(stmt): print("\033[93m {}\033[00m".format(stmt))
def prLightPurple(stmt): print("\033[94m {}\033[00m".format(stmt))
def prPurple(stmt): print("\033[95m {}\033[00m".format(stmt))
def prCyan(stmt): print("\033[96m {}\033[00m".format(stmt))
def prLightGray(stmt): print("\033[97m {}\033[00m".format(stmt))
def prBlack(stmt): print("\033[98m {}\033[00m".format(stmt))


# colored text in slow-fashion
def prSloRed(stmt):
    for letter in stmt:
        print("\033[91m {}\033[00m".format(letter), end="")
        time.sleep(.06)
    print()


def prSloGreen(stmt):
    for letter in stmt:
        print("\033[92m {}\033[00m".format(letter), end="")
        time.sleep(.06)
    print()


def prSloYellow(stmt):
    for letter in stmt:
        print("\033[93m {}\033[00m".format(letter), end="")
        time.sleep(.06)
    print()
    time.sleep(1)


def prSloLightPurple(stmt):
    for letter in stmt:
        print("\033[94m {}\033[00m".format(letter), end="")
        time.sleep(.06)
    print()
    time.sleep(1)


def prSloPurple(stmt):
    for letter in stmt:
        print("\033[95m {}\033[00m".format(letter), end="")
        time.sleep(.06)
    print()


def prSloCyan(stmt):
    for letter in stmt:
        print("\033[96m {}\033[00m".format(letter), end="")
        time.sleep(.06)
    print()
    time.sleep(1)


def prSloLightGray(stmt):
    for letter in stmt:
        print("\033[97m {}\033[00m".format(letter), end="")
        time.sleep(.06)
    print()


def prSloBlack(stmt):
    for letter in stmt:
        print("\033[98m {}\033[00m".format(letter), end="")
        time.sleep(.06)
    print()

