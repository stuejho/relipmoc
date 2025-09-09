from relipmoc.app import add


def test_add():
    res = add(2, 2)
    assert res == 4
