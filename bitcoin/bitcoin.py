import sys
import requests


def get_bitcoin():
    try:
        # בקשת GET ל-API של Coindesk
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        # קריאה לתוכן התשובה כקובץ JSON
        bitcoin_data = response.json()
        # השגת המחיר של הביטקוין
        bitcoin_price = bitcoin_data['bpi']['USD']['rate']
        print(bitcoin_price)
        return float(bitcoin_price.replace(',', ''))  # המרה למספר עשרוני

    except Exception:# as e:
        print("no acsess the json")
        return None

def main():
    # בדיקה האם יש ארגומנט שנכנס לתוכנית
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
        

    try:
        # שליפת המחיר של הביטקוין
        bitcoin_price = get_bitcoin()
        if bitcoin_price is not None:
            # המרה של הארגומנט למספר עשרוני
            argument = float(sys.argv[1])
            # כפל הארגומנט במחיר הביטקוין
            result = argument * bitcoin_price
            # הדפסת התוצאה
            print(f"${result:,.4f}")
    except Exception:
        sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()


