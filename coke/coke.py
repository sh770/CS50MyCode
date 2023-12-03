def main():

    total = 0
    while total < 50:
        print(f"Amount Due: {50 - total}")
        coin = int(input(f"Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            total += coin
            if total < 50:
                print(f"Amount Due: {50 - total}")

                # break

        # else:
        #     print("Invalid coin. Please enter 25, 10 or 5.")

    print(f"Change Owed: {total - 50}")
main()


    # more = int(input("Insert Coin: "))


    # elif more == 45:
    #     print("Amount Due:",5)
    # elif more == 40:
    #     print("Amount Due:",10)
    #  elif more == 35:
    #     print("Amount Due:",15)
    # elif more == 30:
    #     print("Amount Due:",20)
    # if more == 25:
    #     print("Amount Due:",25)
    # if more == 20:
    #     print("Amount Due:",30)
    # if more == 15:
    #     print("Amount Due:",35)
    # if more == 10:
    #     print("Amount Due:",40)
    # if more == 5:
    #     print("Amount Due:",45)
    # if more == 0:
    #     print("Amount Due:",50)
    # more = int(input("Insert Coin: "))

    # if more >= 50:
    #     print("Change Owed:",0)

