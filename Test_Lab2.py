import Lab2 as Lab2

def test_min_max():
    result = []
    result = Lab2.find_min_max([3, 52, 0, 12])
    test_arr = [0, 52]
    assert result == test_arr

def test_average():
    result = Lab2.calc_average([10, 20, 30, 40, 50])
    assert result == 30

def test_median():
    result = Lab2.calc_median_temperature([2, 5, 15, 55])
    assert result == 10