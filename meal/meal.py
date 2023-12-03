def main():
    user_time = input("What time is it? ")

    time = convert(user_time)

    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    if time >= 12.00 and time <= 13.00 :
        print("lunch time")
    if time >= 18.00 and time <= 19.00 :
        print("dinner time")



def convert(time):
    poynt_to_find = "."
    colon_to_find = ":"

    for char in time:
        if char == poynt_to_find:
            hours, minutes = time.split(".")
            break

    for char in time:
        if char == colon_to_find:
            hours, minutes = time.split(":")
            break

    newMin = float(minutes) / 60
    return float(hours) + newMin



if __name__ == "__main__":
    main()

