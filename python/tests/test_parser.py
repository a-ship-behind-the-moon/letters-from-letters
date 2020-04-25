# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import string
import letters_from_letters.parser as parser


def test_parser_detects_2d_default_ok():
    assert parser.is_2d() is True


def test_parser_detects_2d_explicit_ok():
    assert parser.is_2d({"a": "b\nee"}) is True


def test_parser_detects_non_2d_explicit_ok():
    assert parser.is_2d({"a": "bee"}) is False
