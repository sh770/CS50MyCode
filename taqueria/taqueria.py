def main():    
    
    foods ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
    }
    
    

    total_cost  = 0.0
    
    try:
        while True:
            food_name = input("Item: ").lower().title()
            if food_name.lower() in ['quit', 'exit']:  # Allow the user to exit the program
                print("total: $",total_cost)
                print("Exiting the program.")
                break
            
            if food_name in foods:
                total_cost += foods[food_name]
                print(f"total: ${total_cost:.2f}")
            else:
                ...
                # print("Item not on the menu. Please try again.")
    except EOFError:
        print(f"\nOrder complete. Total cost: ${total_cost:.2f}")
    
main()    




