import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
        
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)
    if time:
    
        if time.group(2):
            if int(time.group(2)) >= 60:
                raise ValueError
        if time.group(5):
            if int(time.group(5)) >= 60:
                raise ValueError
    

        
        h1 = int(time.group(1))
        if time.group(3) == "PM" and h1 != 12:
            h1 += 12
        elif time.group(3) == "AM" and h1 == 12:
            h1 -= 12
        if time.group(2) == None:
            t1 = f"{h1:02}:00"
        else:
            t1 = f"{h1:02}:{time.group(2)}"
            
        
        h2 = int(time.group(4)) 
        if time.group(6) == "PM" and h2 != 12:
            h2 += 12
        elif time.group(6) == "AM" and h2 == 12:
            h2 = 12
        if time.group(5) == None: 
            t2 = f"{h2:02}:00"
        else:
            t2 = f"{h2:02}:{time.group(5)}"    
            
        
        time = f"{t1} to {t2}"
        return time 
    else:
        raise ValueError    



if __name__ == "__main__":
    main()