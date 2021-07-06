def readFile(filepath):
    with open(filepath, 'r', encoding="utf-8") as f:
        input = f.read().split('\n')
    print(input)

readFile('test_example1.txt')