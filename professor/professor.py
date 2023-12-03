import random

# lebel = 0

    
def get_level():

        while True:                    
                lebel = input("Level: ")
                try:
                    lebel = int(lebel)                        
                    if 1 <= lebel <= 3:
                        return lebel
                except Exception:
                        pass


def generate_integer(lebel):
        
        score = 0
        
        for i in range(10):
            error_num = 0
            if lebel == 1:
                x = random.randint(0,9)
                y = random.randint(0,9)
            elif lebel == 2:
                x = random.randint(10,99)
                y = random.randint(10,99)
            else:
                x = random.randint(100,999)
                y = random.randint(100,999)
            
            while True:
                answer = input(f"{x} + {y} = ")
                if answer == str(x + y):
                    score += 1
                    break
                elif answer != str(x + y) and error_num != 2:
                    error_num += 1
                    print("EEE")
                    continue
                else:
                    print("EEE")
                    print(f"{x} + {y} = {x + y}")
                    break
        print(score)        
            
        


def main():
    

    
    generate_integer(get_level())   
     

if __name__ == "__main__":
    main()
