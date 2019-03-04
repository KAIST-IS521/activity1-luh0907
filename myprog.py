import sys
import csv

def checkWellFormedCSV(f):
    # Ref:
    # https://stackoverflow.com/questions/2984888/check-if-file-has-a-csv-format-with-python
    try:
        dialect = csv.Sniffer().sniff(f.read(), delimiters=",")
        f.seek(0)
        return dialect
    except csv.Error:
        exit(1)

def parseCSV(f, dialect, N):
    csv_column = []
    csv_reader = csv.reader(f, dialect)
    for row in csv_reader:
        if len(row) < N or N <= 0:
            print("Given column # is not valid.")
            exit(1)
        csv_column.append(row[N-1])

    return csv_column

if __name__ == "__main__":
    if not len(sys.argv) == 3:
        print("Usage: python myprog.py [csvfile] [column #]")
        exit(1)

    filename = sys.argv[1]

    try:
        N = int(sys.argv[2])
    except:
        print("Column # should be an Integer.")
        exit(1)

    try:
        f = open(filename, 'r', errors='ignore')
    except:
        print("Cannot open given input file.")
        exit(1)

    dialect = checkWellFormedCSV(f)
    csv_column = parseCSV(f, dialect, N)

    for item in csv_column:
        print(item)
    
    f.close()
    exit(0)
