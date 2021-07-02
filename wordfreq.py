
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
    markSeps = []
    for word in split:
        markSeps.extend(separateMarks(word, ["!", ",", "."]))
    separated = []
    for word in markSeps:
        separated.extend(separateEnd(word, ['th']))
    return separated

def separateMarks(word: str, marks: list[str]):
    if len(word) == 1:
        return word
    words: list[str] = []

    while True:
        comp = word[-1]
        marksExists = []
        for mark in marks:
            if comp == mark:
                words.append(mark)
                word = word[:-1]
                marksExists.append(True)
            else:
                marksExists.append(False)
        if any(marksExists) == False:
            words.append(word)
            break

    words.reverse()
    return words
#Removes separators from end of list, beginning with the longest alternative
def separateEnd(word: str, seps: list[str]):
    if len(word) == 1:
        return word
    stripWord: str = word
    charCount = len(word)
    words: list[str] = []

    while True:
        for i in range(-len(stripWord), 0, +1):
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


def countWords(words: list[str], skipWords: list[str]):
    wordDict = {}
    if len(words) > 0:
        filtered = [word for word in words if word not in skipWords]
        for word in filtered:
            wordDict[word] = filtered.count(word)
    return wordDict

def printTopMost(wordDict: dict[str, int], top: int):
    if wordDict == {}:
        return {}
    if top < 1:
        return ''
    if top > 0:
        return {key:value for (key,value) in wordDict.items() if value >= top}
    else:
        raise Exception()
