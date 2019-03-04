import sys
import csv

def checkWellFormedCSV(f):
    pass

def parseCSV(f):
    pass

if __name__ == "__main__":
    filename = sys.argv[1]
    N = sys.argv[2]

    f = open(filename, 'r')

    checkWellFormedCSV(f)
    parseCSV(f)
    
    f.close()
