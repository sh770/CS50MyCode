

def main():
    fruit_name = input("Item: ")#.lower()

    fruits = {
    "apple" : "130",
    "Avocado" : "50",
    "Kiwifruit" : "90",
    "Sweet Cherries" : "100",
    "pear" : "100"
    }


    if fruit_name in fruits:
        calorie_value = fruits[fruit_name]
        print(f"Calories: {calorie_value}")



main()
