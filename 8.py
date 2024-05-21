import pytest

from reverse import reverse


@pytest.mark.parametrize('s, expected', [('', ''), ('a', 'a'), ('121', '121'), ('abcd', 'dcba')])
def test_add(s, expected):
    assert reverse(s) == expected
