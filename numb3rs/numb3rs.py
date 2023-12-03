
import sys


def main():
    ip = input("IPv4 Address: ").strip()
    
    print(validate(ip))


def validate(ip):
    
    # try:
    list = ip.split(".")
    
    # print(list)
    # print(len(list))
    if len(list) != 4:
        return False
    
    for s in list:
        if int(s) > 255:
            print(s)
            return False
        # else:
        #     print(s)
        #     return True
    # print(1)
    return True    
        
        # comment: 
    # except Exception :
    #     sys.exit("no ip valid") 
    # end try
    
    
    # return 2
    
    # ...





if __name__ == "__main__":
    main()