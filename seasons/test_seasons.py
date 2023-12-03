from seasons import minut_live

def test_seasons():

    assert minut_live(2000, 2, 2) == "Twelve million, five hundred sixteen thousand, four hundred eighty minutes"
    assert minut_live(29, 1, 2983) == "Invalid Date"