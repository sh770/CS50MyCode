from plates import is_valid

def main():
    test_is_valid()
    

def test_is_valid():
    assert is_valid("CS50")
    assert not is_valid("CS05")
    assert not is_valid("CS50P")
    assert not is_valid("6S50P")
    assert not is_valid("PI3.14")
    assert not is_valid("H")
    assert not is_valid("OUTATIME")
    assert not is_valid("cfgcgfcf")
    assert not is_valid("11")


if __name__ == "__main__":
    main()