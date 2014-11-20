#!/usr/bin/env python
"""MMM TOASTY."""
import os
import random
import sys
import time


class Color(object):
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


EYES = ''.join((
    '3$$$F "$$',
    Color.END,
    "O",
    Color.RED,
    '$b   $"$$$$$',
    Color.END,
    "O",
    Color.RED,
    '$  $$$$*"',
))
SKULL = '\n'.join((
    '      .ed"""" """$$$$be.',
    '     -"           ^""**$$$e.',
    '   ."                   \'$$$c',
    '  /                      "4$$b',
    ' d  3                      $$$$',
    ' $  *                   .$$$$$$',
    '.$  ^c           $$$$$e$$$$$$$$.',
    'd$L  4.         4$$$$$$$$$$$$$$b',
    '$$$$b ^ceeeee.  4$$ECL.F*$$$$$$$',
    '$$$$P d$$$$F $ $$$$$$$$$- $$$$$$',
    EYES,
    ' $$P"  "$$b   .$ $$$$$...e$$$$',
    '  *c    ..    $$ 3$$$$$$$$$$eF',
    '    %ce""    $$$  $$$$$$$$$$*',
    '     *$e.    *** d$$$$$"L$$',
    '      $$$      4J$$$$$% $$$',
    '     $"\'$=e....$*$$**$cz$$"',
))
LAUGH = '\n'.join((
    '',
    '     $$$                $$',
    '      $$$             $$$$'
))
JAW = '\n'.join((
    '',
    '     $  *=%4.$ L L$ P3$$$F',
    '     $   "%*ebJLzb$e$$$$$b',
    '      %..      4$$$$$$$$$$',
    '       $$$e   z$$$$$$$$$$',
    '        "*$c  "$$$$$$$P"',
    '          """*$$$$$$$"'
))

CREDITS = [
    "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "CREDITS", " ", "MMM... TOASTY", " ", "BY", " ",
    "BEST NATION SERBIA WARRIORS", " ", "WE CREATE HELL FOR CROAT", " ",
    "FUCK TO CROAT SWINE", " ", "SERBIA NUMBER 1", " ",
    "HACK SQUAD CHECKMATE 1992", " ", "GREETINGS TO:", " ",
    "HACK BABY, DIGITAL MAN 1994, MR. FAT, TONY,",
    "TRANCE PRINCE, GHOST WOMAN, BIO HOG, TAD", " ",
    "FUCK TO CROAT !! IT IS A SHIT TO ME", "", "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
]

TOASTY_TEXT = "\n          Mmmm... Toasty"

CRACK = (
    "\n       PROGRAM IS CRACK BY"
    "\n    HACK SQUAD CHECKMATE 1992"
    "\n        SERBIA BEST NATION\n"
)

MT = 69
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    MT = int(sys.argv[1])

for i in range(25):
    print '\033[1;37;' + str(random.randint(41, 46)) + 'm' + (" " * 50)
    time.sleep(0.05)
    if i == 12:
        print (
            "\033[1;37;41m###############   YOU     ARE  ###################"
        )
    if i == 13:
        print (
            "\033[1;37;41m##############   MOTHER FUCKER   #################"
        )
print '\033[0m'
time.sleep(1)
os.system('clear')

for i in range(MT):
    if i % 2 == 0:
        print Color.RED + SKULL + JAW + Color.END + TOASTY_TEXT + CRACK
    else:
        print Color.RED + SKULL + LAUGH + JAW + Color.END + TOASTY_TEXT + CRACK
    time.sleep(0.4)
    os.system('clear')

while len(CREDITS) > 1:
    for i in range(25):
        if len(CREDITS) < 25:
            exit()
        print CREDITS[i]
    time.sleep(0.2)
    os.system('clear')
    CREDITS.pop(0)
