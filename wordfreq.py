
def tokenize(inputList: list):
    if not isinstance(inputList, list):
        raise Exception('You have to enter an list')
    if inputList == []:
        return []
    filtered = [line for line in inputList if line !=
                '' and line.isspace() == False]
    if len(filtered) == 0:
        return []
    split = [item for sublist in unpack(filtered) for item in sublist]
    separated = []
    for word in split:
        separated.extend(separate(word, ['!', 'th']))
    return separated


def separate(word: str, seps: list[str]):
    # if len(word) == 1:
    #     return word
    stripWord: str = word
    charCount = len(word)
    words: list[str] = []
#Removes separators from end of list, beginning with the longest
    while True:
        start = -len(stripWord)
        end = 0
        iRange = range(start, end, +1)
        rangeList = [i for i in iRange]
        for i in iRange:
            comp = stripWord[i:]
            for sep in seps:
                if comp == sep:
                    words.append(sep)
                    stripWord = stripWord.strip(sep)
        if len(stripWord) == charCount:
            words.insert(0, stripWord)
            break
        else:
            charCount = len(stripWord)
    return words


def unpack(input):
    if isinstance(input, str):
        if ' ' in input:
            return [word.lower() for word in input.split()]
        else:
            return input.lower()
    if isinstance(input, list):
        return [unpack(item) for item in input]


def countWords():
    pass


def printTopMost():
    pass
