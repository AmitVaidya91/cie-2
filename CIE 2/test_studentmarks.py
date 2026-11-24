from app import calculate
def test_calculate():
    total,percentage,average = calculate(10,20.30)
    assert total == 60
    assert average == 30
    assert percentage == 30
