def main():

    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    # print(user_input)


    if user_input.strip() == "42" or user_input.strip() == "forty-two" or user_input.strip() == "forty two" or user_input == "FoRty TwO":
        print("yes")
    else:
        print("no")


main()
