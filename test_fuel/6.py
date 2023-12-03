# פונקציה ראשית
def main():
    while True:
        try:
            # קריאה לפונקציה המשנה לטיפול בקלט וחישוב התוצאה
            result = process_fraction_input()

            # בדיקת קטגוריה והדפסה/החזרה
            if result == "E":
                print("E")
                return "E"
            elif result == "F":
                print("F")
                return "F"
            else:
                print(result)
                return result

            # הוצאת התוכנית מהלולאה במקרה של קלט תקין
            break

        except (ValueError, ZeroDivisionError):
            raise("Invalid input. Please enter a fraction X/Y where X and Y are integers and Y is not zero.")

# פונקציה משנה לטיפול בקלט וחישוב התוצאה
def process_fraction_input():
    fraction = input("Fraction: ")
    x, y = map(int, fraction.split('/'))

    # בדיקת שתי התנאים: אם הפונקציה יחזירה "E" והפונקציה יחזירה "F"
    category = convert((x / y) * 100)
    return gauge(category)

# פונקציה להמרה של אחוז לקטגוריה
def convert(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        # החזרת התוצאה בפורמט של אחוז מעוגל
        return f"{round(percentage)}"

# פונקציה להמרת קטגוריה לתוצאה סופית
def gauge(category):
    if category == "E":
        return "E"
    elif category == "F":
        return "F"
    else:
        return f"{category}%"

# התנאי המוודא שהקוד יתרץ רק כאשר הקובץ יופעל ישירות ולא ייובא כמודול
if __name__ == "__main__":
    # קריאה לפונקציה הראשית main כאשר התוכנית מופעלת
    main()
