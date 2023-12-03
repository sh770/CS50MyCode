import random
import sys


def main():
    try:
        while True:
            user_input = input("Level: ").strip()
            try:
                number = int(user_input)
                range = random.randint(1, number)
                # if 1 <= number <= 100:
                #     break
                # print(f"המספר שהוזן הוא: {number}")
                break  # יציאה מהלולאה אם המספר תקין
            except ValueError:
                pass
                # print("הזנת משהו שאינו מספר שלם. נסה שוב.")
    except KeyboardInterrupt:

        pass
    try:
        while True:
            user_int = input("Guess: ").strip()
            try:
                user_int = int(user_int)
                # if 1 <= user_int <= 100:
                if user_int < range:
                    print("Too small!")
                    continue
                elif user_int > range:
                    print("Too large!")
                    continue
                elif user_int == range:
                    sys.exit("Just Right!")
                    print("Just right!")
                    break
                else:
                    break
            except ValueError:
                pass
                # print("******##########*****")
    except EOFError:
        print("***********")
        # break
        main()
