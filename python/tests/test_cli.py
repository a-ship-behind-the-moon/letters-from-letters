# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import string
import letters_from_letters.cli as cli


def test_cli_rot13_ok():
    command, a, b, z = "ROT13", "A", "B", "Z"
    argv = ["ignore", command, a, b, z]
    m_a, m_b, m_z = cli.main(argv)
    assert m_a == "N"
    assert m_b == "O"
    assert m_z == "M"


def test_cli_rot13_spaces_ok():
    command, a, b, e, sp = "ROT13", "A", "b", "e", " "
    argv = ["ignore", command, a, sp, b, e, e]
    rotated = cli.main(argv)
    assert rotated == ('N', ' ', 'o', 'r', 'r')


def test_cli_rot13_phrase_ok():
    command, phrase = "ROT13", "A bee"
    argv = ["ignore", command, phrase]
    rotated = cli.main(argv)
    assert rotated == ('N orr',)


def test_cli_rot13_words_ok():
    command, a, sp, bee = "ROT13", "A", " ", "bee"
    argv = ["ignore", command, a, sp, bee]
    rotated = cli.main(argv)
    assert rotated == ('N', ' ', 'orr')


def test_cli_map_ok():
    a, b, z = "A", "B", "Z"
    argv = ["ignore", a, b, z]
    m_a, m_b, m_z = cli.main(argv)
    assert m_a == "\n    A  \n   A A   \n  AAAAA   \n A     A"
    assert m_b == "\n BBBB  \n B    B  \n BBBB     \n B    B \n BBBB "
    assert m_z == "\n  ???? \n ?    ?  \n    ?     \n    ?   \n       \n    ?   "


def test_cli_map_phrase_ok():
    phrase = "A bee"
    argv = ["ignore", phrase]
    mapped = cli.main(argv)
    assert mapped == ('\n  ???? \n ?    ?  \n    ?     \n    ?   \n       \n    ?   ',)


def test_cli_map_words_ok():
    a, sp, bee = "A", " ", "bee"
    argv = ["ignore", a, sp, bee]
    mapped = cli.main(argv)
    assert mapped == ('\n    A  \n   A A   \n  AAAAA   \n A     A',
                      '\n       \n         \n          \n        ',
                      '\n  ???? \n ?    ?  \n    ?     \n    ?   \n       \n    ?   ')


def test_cli_random_seed_ok():
    command, seed, a, b, z = "RNG", "42", "A", "B", "Z"
    argv = ["ignore", command, seed, a, b, z]
    m_a, m_b, m_z = cli.main(argv)
    assert m_a == "J"
    assert m_b == "W"
    assert m_z == "O"


def test_cli_random_phrase_ok():
    command, seed, phrase = "RNG", "42", "A bee"
    argv = ["ignore", command, seed, phrase]
    shuffled = cli.main(argv)
    assert shuffled == ('J', '?', 'x', 'v', 'v')


def test_cli_random_words_ok():
    command, seed, a, sp, bee = "RNG", "42", "A", " ", "bee"
    argv = ["ignore", command, seed, a, sp, bee]
    shuffled = cli.main(argv)
    assert shuffled == ('J', '?', 'x', 'v', 'v')


def test_cli_random_really_ok():
    command, a, b, z = "RNG", "A", "B", "Z"
    argv = ["ignore", command, a, b, z]
    m_a, m_b, m_z = cli.main(argv)
    assert m_a in string.ascii_letters
    assert m_b in string.ascii_letters
    assert m_z in string.ascii_letters
    assert m_a != m_b
    assert m_b != m_z


def test_cli_random_really_phrase_ok():
    command, phrase = "RNG", "A bee"
    argv = ["ignore", command, phrase]
    really_random = cli.main(argv)
    assert really_random[0] in string.ascii_letters
    assert really_random[1] == '?'
    assert all(c in string.ascii_letters for c in really_random[2:])
    for n, c in enumerate(really_random):
        for m, d in enumerate(really_random):
            if n != m:
                assert c != d or phrase[n] == phrase[m], f"{c}, {d}, {n}, {m}, {phrase[n]}, {phrase[m]}"


def test_cli_random_really_words_ok():
    command, a, sp, bee = "RNG", "A", " ", "bee"
    argv = ["ignore", command, a, sp, bee]
    really_random = cli.main(argv)
    assert really_random[0] in string.ascii_letters
    assert really_random[1] == '?'
    assert all(c in string.ascii_letters for c in really_random[2:])
