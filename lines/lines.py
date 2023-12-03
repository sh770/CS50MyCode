import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
    
py = sys.argv[1]
if not ".py" in py:
    sys.exit("Not a Python file")
else:
    
    
    try:
        with open(py) as file:
            count = 0
            for line in file:
                if not line.strip().startswith("#") and line.strip() != "":
                    count += 1
            print(count)    

    except FileNotFoundError:
        sys.exit("File does not exist")
        




 