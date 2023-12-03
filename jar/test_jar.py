from jar import Jar


def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0
    
    
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(8)
    assert jar.size == 8


def test_withdraw():
    jar = Jar(10)
    jar.deposit(9)
    jar.withdraw(8)
    assert jar.size == 1
    