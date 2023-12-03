def main():

    try:
        list_grocery = {}
        while True:
            try:

                item_user_input = input("").strip().upper()
                if item_user_input:
                    list_grocery[item_user_input] = list_grocery.get(item_user_input, 0) + 1

            except EOFError:
                break
        for item in sorted(list_grocery):
            print(f"{list_grocery[item]} {item}")




    except KeyboardInterrupt:
        print("\nInput interrupted by user.")






main()
