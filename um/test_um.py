from um import count

def test_count():
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks for the album.") == 1
    assert count("hello, um, world") == 1
    assert count("hello, world") == 0