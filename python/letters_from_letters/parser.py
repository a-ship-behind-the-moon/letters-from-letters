"""Letters from letters - loader/parser."""
import codecs
import json
import os
import random  # pylint: disable=syntax-error
import string  # pylint: disable=syntax-error


DATA_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(DATA_FOLDER, "letter_map.json")
ENCODING = "utf-8"
MAP = json.load(open(DATA_PATH, encoding=ENCODING))
_VAP = list(string.ascii_letters)
random.shuffle(_VAP)
RAP = {x: y for x, y in zip(list(string.ascii_letters), _VAP)}


def letter(char):
    """Derive letter from char."""
    return MAP.get(char)


def rot_13(char):
    """Special case of shift alphabet by half."""
    return codecs.encode(char, "rot_13")


def random_n(char, seed=None):
    """Random shuffle."""
    if seed is None:
        return RAP.get(char, "?")
    _vap = list(string.ascii_letters)
    random.seed(seed)
    random.shuffle(_vap)
    inefficient = {x: y for x, y in zip(list(string.ascii_letters), _vap)}
    return inefficient.get(char, "?")
