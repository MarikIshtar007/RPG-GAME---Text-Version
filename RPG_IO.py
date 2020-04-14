import time


def print_title(str):
    for letter in str:
        print(letter, end="")
        time.sleep(.000002)
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


def prSloLightPurple(stmt):
    for letter in stmt:
        print("\033[94m {}\033[00m".format(letter), end="")
        time.sleep(.06)
    print()


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
2