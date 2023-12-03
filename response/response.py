import validators
# import sys

def main():
    mail = input("What's your email address? ").lower().strip()
    
    # print(validators.email('someone@example.com'))
    if validators.email(mail):
        print("Valid")
    else:
        print("Invalid")

    
if __name__ == "__main__":
    main()