from twttr import shorten
    
def main():
    test_twttr()
    

def test_twttr():
    assert shorten("hello") ==  "hll"
    assert shorten("HELLO") ==  "HLL"
    assert shorten("01") ==  "01"
    assert shorten(",.-_") ==  ",.-_"
    
if __name__ == "__main__":
    main()

# def test_twttr():
#     assert shorten("hello") ==  "hll"
#     assert shorten("HELLO") ==  "HLL"
#     assert shorten("01") ==  "01"
#     assert shorten(",.-_") ==  ",.-_"
    