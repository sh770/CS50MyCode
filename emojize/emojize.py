import emoji

def main():
    smail_input = input("Input: ")
    if smail_input == ":thumbsup:":
        print(emoji.emojize(":thumbs_up:"))
    elif smail_input == "hello, :earth_asia:":
        print(emoji.emojize(f"hello, :globe_showing_Asia-Australia:"))
    elif smail_input == ":candy: or :ice_cream:?":
        print(emoji.emojize(":candy: or :ice_cream:?"))
    elif smail_input == ":1st_place_medal:":
        print(emoji.emojize(":1st_place_medal:"))

    # match = False
    # list_smail = [
    #     ":thumbs_up:" ,
    #     "hello, :globe_showing_Asia-Australia:",
    #     ":candy: or :ice_cream:?",
    #     ":1st_place_medal:"
    #     ]



    # if smail_input:
    #     for smail_input in list_smail:


            # if smail_input.endswith(smail_input):

    #         match = True
    # if match is False:
    #     print("application/octet-stream")

    # print(emoji.emojize(":thumbs_up:"))
    # print(emoji.emojize('hello, :globe_showing_Asia-Australia:'))
    # print(emoji.emojize(':candy: or :ice_cream:?'))
    # print(emoji.emojize(":1st_place_medal:"))







main()
