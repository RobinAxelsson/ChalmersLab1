import enum

class strType(enum.Enum):
    Alpha = 0
    Digit = 1
    Symbol = 2
    White = 3
    
    def checkType(char: str):
        if char.isspace():
            return strType.White
        if char.isdigit():
            return strType.Digit
        if char.isalpha():
            return strType.Alpha
        else:
            return strType.Symbol

def tokenize(input):
    if input == []:
        return []
    if isinstance(input, list):
        input = " ".join(input)
    words = [word.lower() for word in input.split()]
    output = []
    for word in words:
        output.extend(typeSplit(word))
    return output

def typeSplit(word: str):
    output: list[str] = []
    temp = ''
    lastType = strType.Alpha

    for char in word:
        newType = strType.checkType(char)

        # all symbols are seperated from each other in a new string
        if newType == strType.Symbol:
            if temp != '':
                output.append(temp)
            output.append(char)
            temp=''
            lastType = strType.Symbol

        # whites are allways skipped
        elif newType == strType.White:
            if temp != '':
                output.append(temp)
            temp=''
        # if new chartype is different from last save the
        # temporary string and start building a new one
        elif newType != lastType:
            if temp != '':
                output.append(temp)
            temp = char
            lastType = newType
        elif newType == strType.Alpha or newType == strType.Digit:
            temp+=char

    if temp != '':
        output.append(temp)
    return output

def countWords(words: list[str], skipWords: list[str]):
    skipWords = tokenize(skipWords)
    wordDict = {}
    if len(words) > 0:
        filtered = [word for word in words if word not in skipWords]
        for word in filtered:
            wordDict[word] = filtered.count(word)
    return wordDict

def printTopMost(wordDict: dict[str, int], top: int):
    if wordDict == {} or top < 1:
        return
    tupleFreq = [(word, freq) for word, freq in wordDict.items()]
    tupleFreq.sort(key=lambda tup: tup[1], reverse=True)
    concats = []
    if top > len(tupleFreq):
        top = len(tupleFreq)
    for i in range(top):
        word = tupleFreq[i][0]
        freq = str(tupleFreq[i][1])
        whiteCount = 25-len(word)-len(freq)
        concats.append(word + ' '*whiteCount + freq)
    print('\n'.join(concats))
