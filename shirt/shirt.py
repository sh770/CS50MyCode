import sys 
from PIL import Image ,ImageOps 


def main():
    
    check_argv()
    
    check_file_type()
    
    shirt_fix()
    
    

def check_argv():
    
    if len(sys.argv) == 3:
        return sys.argv
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too many command-line arguments")
        
def check_file_type(): 
  
    try:
        allowed_formats = [".jpg", "jpeg", ".png"]

        file_1_format = sys.argv[1][-4:]
        file_2_format = sys.argv[2][-4:]
        user_img = Image.open(sys.argv[1])
        if sys.argv[1][-4:] not in allowed_formats:
            sys.exit("Invalid input")

        elif file_1_format is None or file_2_format is None:
            sys.exit("Invalid input")
            
        elif file_1_format != file_2_format:
            sys.exit("Input and output have different extensions")
        else:
            return
        
    except ValueError:
        pass
        sys.exit("Invalid input")
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]} does not exist")
            


def shirt_fix():
    
    shirt = Image.open("shirt.png")
    
    user_img = Image.open(sys.argv[1])
    
    size = shirt.size
    
    user_img = ImageOps.fit(user_img, size)
    
    user_img.paste(shirt, shirt)
    
    user_img.save(sys.argv[2])
    
    
    
if __name__ == "__main__":
    main()
    
  