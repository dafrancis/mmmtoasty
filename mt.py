#!/usr/bin/env python
"""MMM TOASTY."""
import os
import random
import sys
import time


class Color(object):
    """Color enum for showing terminal colors."""
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

    @classmethod
    def random_background(cls):
        """String to set the terminal background to a random color."""
        return '\033[1;37;' + str(random.randint(41, 46)) + 'm'


class Skull(object):
    """Skull animation manager."""
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
    TOASTY_TEXT = "\n          Mmmm... Toasty"
    CRACK = (
        "\n       PROGRAM IS CRACK BY"
        "\n    HACK SQUAD CHECKMATE 1992"
        "\n        SERBIA BEST NATION\n"
    )

    @classmethod
    def closed_mouth(cls):
        """Closed Mouth."""
        return ''.join((
            Color.RED,
            cls.SKULL,
            cls.JAW,
            Color.END,
            cls.TOASTY_TEXT,
            cls.CRACK,
        ))

    @classmethod
    def open_mouth(cls):
        """Open Mouth."""
        return ''.join((
            Color.RED,
            cls.SKULL,
            cls.LAUGH,
            cls.JAW,
            Color.END,
            cls.TOASTY_TEXT,
            cls.CRACK
        ))

    @classmethod
    def animate(cls, cycles):
        """Animate the skull."""
        for i in range(cycles):
            if i % 2 == 0:
                print cls.closed_mouth()
            else:
                print cls.open_mouth()
            time.sleep(0.4)
            os.system('clear')

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


def get_toasty_number():
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        return int(sys.argv[1])
    return 69


def display_intro():
    for i in range(25):
        print Color.random_background() + (" " * 50)
        time.sleep(0.05)
        if i == 12:
            print (
                "\033[1;37;41m###############   YOU     ARE  ###################"
            )
        if i == 13:
            print (
                "\033[1;37;41m##############   MOTHER FUCKER   #################"
            )
    print Color.END
    time.sleep(1)
    os.system('clear')


def display_credits():
    while len(CREDITS) > 1:
        for i in range(25):
            if len(CREDITS) < 25:
                exit()
            print CREDITS[i]
        time.sleep(0.2)
        os.system('clear')
        CREDITS.pop(0)

if __name__ == '__main__':
    MT = get_toasty_number()
    display_intro()
    Skull.animate(MT)
    display_credits()
