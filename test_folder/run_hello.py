import sys

filepath = sys.argv[1]
with open(filepath, 'r', encoding="utf-8") as f:
            print(f.read())