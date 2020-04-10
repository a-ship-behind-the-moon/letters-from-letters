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


def test_cli_map_ok():
    a, b, z = "A", "B", "Z"
    argv = ["ignore", a, b, z]
    m_a, m_b, m_z = cli.main(argv)
    assert m_a == "\n    A  \n   A A   \n  AAAAA   \n A     A"
    assert m_b == "\n BBBB  \n B    B  \n BBBB     \n B    B \n BBBB "
    assert m_z == "\n  ???? \n ?    ?  \n    ?     \n    ?   \n       \n    ?   "


def test_cli_random_seed_ok():
    command, seed, a, b, z = "RNG", "42", "A", "B", "Z"
    argv = ["ignore", command, seed, a, b, z]
    m_a, m_b, m_z = cli.main(argv)
    assert m_a == "J"
    assert m_b == "W"
    assert m_z == "O"


def test_cli_random_really_ok():
    command, a, b, z = "RNG", "A", "B", "Z"
    argv = ["ignore", command, a, b, z]
    m_a, m_b, m_z = cli.main(argv)
    assert m_a in string.ascii_letters
    assert m_b in string.ascii_letters
    assert m_z in string.ascii_letters
    assert m_a != m_b
    assert m_b != m_z
