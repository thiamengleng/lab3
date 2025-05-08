import lab2.bmi as bmi
    
def test_under_weight():
    assert(bmi.calculate_bmi(1.73, 50) == -1)
    assert(bmi.calculate_bmi(1.9, 40) == -1)
    assert(bmi.calculate_bmi(1.73, 50) == -1)
    assert(bmi.calculate_bmi(2, 50) == -1)
    assert(bmi.calculate_bmi(1.53, 40) == -1)
    assert(bmi.calculate_bmi(1.2, 21) == -1)
def test_normal_weight():
    assert(bmi.calculate_bmi(1.8, 71) == 0)
    assert(bmi.calculate_bmi(1.73, 62) == 0)
def test_over_weight():
    assert(bmi.calculate_bmi(1.23, 100) == 1)
    assert(bmi.calculate_bmi(1.63, 90) == 1)
    assert(bmi.calculate_bmi(1.5, 70) == 1)
    assert(bmi.calculate_bmi(1.73, 81) == 1)
