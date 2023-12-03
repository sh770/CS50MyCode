def main():
    
    bank_say = input("Greeting: ")
    greeting = bank_say.strip().lower()
    print(f"${value(greeting)}")
    

def value(greeting):     
    word = "hello"
    # print(bank_bles)
    if greeting.startswith(word):
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100
  

if __name__ == "__main__":
    main()



# def main():


#     bank_say = input("Greeting: ")
#     # print(bank_say)

#     bank_bles = bank_say.strip().lower()

#     # print(bank_bles[0])
#     word = "hello"
#     # print(bank_bles)
#     if bank_bles.startswith(word):
#         print("$0")
#     elif bank_bles[0] == "h":
#         print("$20")
#     else:
#         print("$100")



# main()


