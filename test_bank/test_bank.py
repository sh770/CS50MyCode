from bank import value

    
def main():
    test_bank()
    
def test_bank():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hou ar u") == 20
    assert value("world") == 100
    assert value("wea't up?") == 100
    assert value("123") == 100
    assert value("  123   ") == 100
    assert value("  grg   ") == 100


    
    
if __name__ == "__main__":
    main()