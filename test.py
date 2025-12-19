from calculator import calculate_area


def test_calculate_area():
    assert calculate_area(5, 10) == 50
    assert calculate_area(0, 10) == 0
    assert calculate_area(7, 3) == 21
