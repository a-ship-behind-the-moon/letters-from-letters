# -*- coding: utf-8 -*-
"""Command line arg for the letter mapping toy."""
from itertools import chain
import string  # pylint: disable=syntax-error
import sys
import letters_from_letters.parser as parser


def main(argv=None):
    """Drive the understanding ..."""
    argv = sys.argv if argv is None else argv
    if len(argv) > 2 and argv[1].lower() in ("rot13", "rot_13"):
        return tuple(parser.rot_13(char) for char in argv[2:])
    if len(argv) >= 3 and argv[1].lower() in ("random", "rand", "rng"):
        if all(n in string.digits for n in argv[2]) and len(argv) > 3:
            return tuple(parser.random_n(char, int(argv[2])) for char in chain.from_iterable(argv[3:]))
        return tuple(parser.random_n(char) for char in chain.from_iterable(argv[2:]))

    return tuple(parser.letter(char) or parser.MAP["?"] for char in argv[1:])
