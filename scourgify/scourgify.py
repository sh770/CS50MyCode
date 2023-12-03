import csv
import sys


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 4:
    sys.exit("Too many command-line arguments")
    
tabel = sys.argv[1]
if not ".csv" in tabel:
    sys.exit(f"Could not read {tabel}")
else:    
    
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            # print(reader)
            with open(sys.argv[2], "w") as file2:
                writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    row["first"] = row.pop("name")
                    last_name , first_name = row["first"].split(", ")
                    row["first"] = first_name
                    row["last"] = last_name
                    writer.writerow(row)

                    

    except FileNotFoundError:
        sys.exit(f"Could not read {tabel}")
        

