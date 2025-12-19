from contain_five import contains_five


def test_contains_five():
    assert contains_five([1, 2, 3, 4, 5]) is True
    assert contains_five([0, -1, -2, -3]) is False
    assert contains_five([5, 5, 5]) is True
    assert contains_five([]) is False
