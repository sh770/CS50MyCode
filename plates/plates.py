def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        return "Valid"
    else:
        print("Invalid")
        return "Invalid"
    

def is_valid(plate):

    if len(plate) < 2 or len(plate) > 6:
        return False



    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False


    if not plate.isalnum():
        return False


    num_start = False
    for char in plate[2:]:
        if char.isdigit():
            num_start = True
            if char == "0" and plate[2] == char:
                return False
        elif num_start: 
            return False

    return True





main()
