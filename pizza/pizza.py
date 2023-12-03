import sys , csv ,tabulate


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
    
tabel = sys.argv[1]
if not ".csv" in tabel:
    sys.exit("Not a CSV file")
else:    
    
    try:
        with open(tabel) as file:
            reader = csv.DictReader(file)
            print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))
            # print(reader)
  

    except FileNotFoundError:
        sys.exit("File does not exist")
        




 