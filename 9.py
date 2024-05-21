import pytest


def count_chars(s):
    pass


def test_empty_string():
    result = count_chars('')
    assert result == {}


def test_single_character_string():
    result = count_chars('a')
    assert result == {'a': 1}


def test_multiple_characters_string():
    result = count_chars('hello')
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}


def test_repeated_characters_string():
    result = count_chars('mississippi')
    assert result == {'m': 1, 'i': 4, 's': 4, 'p': 2}


def test_non_string_input():
    with pytest.raises(TypeError):
        count_chars(123)


def test_iterable_non_string_input():
    with pytest.raises(TypeError):
        count_chars([1, 2, 3])
