
def main():
    word = input("Input: ")
    print(shorten(word))
    # ...


def shorten(word):
    word = (
    word
    .replace("a", "")
    .replace("e", "")
    .replace("i", "")
    .replace("o", "")
    .replace("u", "")
    .replace("A", "")
    .replace("E", "")
    .replace("I", "")
    .replace("O", "")
    .replace("U", "")
)

    return(word)
    ...


if __name__ == "__main__":
    main()

# def main():
#     strng_user_input = input("Input: ")

#     strng_user_input = (
#     strng_user_input
#     .replace("a", "")
#     .replace("e", "")
#     .replace("i", "")
#     .replace("o", "")
#     .replace("u", "")
#     .replace("A", "")
#     .replace("E", "")
#     .replace("I", "")
#     .replace("O", "")
#     .replace("U", "")
# )

#     print(strng_user_input)





# if __name__ == "__main__":
#     main()
