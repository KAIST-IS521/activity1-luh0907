import sys
import csv

def checkWellFormedCSV(f):
    # Ref:
    # https://stackoverflow.com/questions/2984888/check-if-file-has-a-csv-format-with-python
    try:
        dialect = csv.Sniffer().sniff(f.read())
        f.seek(0)
    except csv.Error:
        exit(1)

def parseCSV(f):
   pass 

if __name__ == "__main__":
    if not len(sys.argv) == 3:
        print("Usage: python myprog.py [csvfile] [column #]\n")
        exit(1)

    filename = sys.argv[1]
    N = sys.argv[2]

    try:
        f = open(filename, 'r')
    except:
        print("Cannot open given input file.\n")
        exit(1)

    checkWellFormedCSV(f)
    parseCSV(f)
    
    f.close()
