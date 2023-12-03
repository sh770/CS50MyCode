def main():
    months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
    }

    # מחזיר את המספר המתאים לשם החודש מהמילון
    def get_month_number(month_name):
        return months.get(month_name)

    while True:
        data = input("Date: ").strip()
        # if not "," in data:# or not "/" in data:
        #     print("-------------")
        #     break
        # else:
        #     print("----2---------")
        #     continue
        if "," in data:
            # print(data)
            data = data.replace(",", " ")
            # print(data)
            month_name, day, year = data.split()
            if month_name in months:
                month_name = get_month_number(month_name)
                # print(month_name, day, year)
                # print("---------------")
        elif "/" in data:
            month_name, day, year = data.split("/")
        else:
            continue

        try:
            if int(month_name) > 12 or int(day) > 31:
                continue
            else:
                break
        except ValueError:
            continue


    print(year + "-" + f"{int(month_name):02}" + "-" + f"{int(day):02}")



main()
