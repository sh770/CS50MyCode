from datetime import date
import sys, inflect

p = inflect.engine()

def main():
    
    try:
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid date")
    
    print(minut_live(year, month, day))


def minut_live(year, month, day):
    
    try:
        tm = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")
    # print(tm)   
    
    tday = date.today() 
    
    # print(tday)
    
    dif = tday - tm
    
    min = int(dif.total_seconds() / 60)
    
    tot = p.number_to_words(min, andword="") + " minutes"
    
    return tot.capitalize()
    
    
    
        

if __name__ == "__main__":
    main()