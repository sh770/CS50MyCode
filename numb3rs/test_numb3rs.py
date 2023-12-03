from numb3rs import validate

def test_validate():
    assert validate("1.1.1.1")
    assert not validate("1.1.1")
    assert not validate("dog")
    assert not validate("1.1.1.257")
    assert not validate("1.1.1.1.1")