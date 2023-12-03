import inflect

p = inflect.engine()

names = ["Adieu", "adieu"]    
def main():
    


    
    try:
        while True:
            names_add = input("Name: ")
        
            names.append(names_add)
    except EOFError:        
        print()
        
        
    names[2] = "to " + names[2]

    
    

      
    if len(names) == 3:
        n_names = p.join(names, conj='')
    elif len(names) == 4:   
        n_names = p.join(names, final_sep='')
    else:
        n_names = p.join(names)
        

    print(n_names)


main()