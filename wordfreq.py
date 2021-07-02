
def tokenize(inputList: list):
    if not isinstance(inputList, list):
        raise Exception('You have to enter an list')
    if inputList == []:
         return []
    filtered = [line for line in inputList if line != '' and line.isspace() == False]
    if len(filtered) == 0:
        return []
    split = [item for sublist in unpack(filtered) for item in sublist]
    separated = []
    for word in split:
        separated.extend(separate(word, ['!', 'th']))
    return separated

def separate(word: str, seps: list[str]):
    stripWord: str = word
    wordIndexes: list[(str, int)] = list()
    for sep in seps:
        if sep in word:
            wordIndexes.append((sep, word.index(sep)))
            stripWord = stripWord.strip(sep)
    wordIndexes.append((stripWord, word.index(stripWord)))
    sortedWords: list[str] = [x[0] for x in sorted(wordIndexes, key=lambda w: w[1])]
    return sortedWords

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