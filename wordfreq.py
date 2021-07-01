
def tokenize(words: list):
    outWords = []
    for word in words:
        if check(word):
            outWords.append(word)

    return outWords

def check(word: str):
    if word.isspace():
        return False
    if word is '':
        return False
    else:
        return True

def countWords():
    pass

def printTopMost():
    pass