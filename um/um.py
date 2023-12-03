import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    
        
    # מצא את כל ההתאמות בטקסט
    matches = re.findall(r'\bum\b', s, re.IGNORECASE)
    
    # החזרת מספר ההתאמות
    return len(matches)
    


if __name__ == "__main__":
    main()