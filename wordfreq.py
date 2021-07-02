# Your first task is to define a function called tokenize which should take a 
# complete document as a list of text lines and produce a list of tokens, in the correct order.
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
    output = []
    for word in split:
        output.extend(typeSplit(word))
    return output
    
def unpack(input):
    if isinstance(input, str):
            return typeSplit(input.lower())
    if isinstance(input, list):
        return [unpack(item) for item in input]
    else:
        raise Exception()

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
    wordDict = {}
    if len(words) > 0:
        filtered = [word for word in words if word not in skipWords]
        for word in filtered:
            wordDict[word] = filtered.count(word)
    return wordDict

def printTopMost(wordDict: dict[str, int], top: int):
    if wordDict == {}:
        return wordDict
    if top > 0 and len(wordDict)>0:
        tupleFreq = [(word, freq) for word, freq in wordDict.items()]
        tupleFreq.sort(key=lambda tup: tup[1], reverse=True)
        strList: list[str] = []
        for i in range(top):
            word = tupleFreq[i][0]
            freq = str(tupleFreq[i][1])
            freq = freq.rjust(26-len(freq)-len(word))
            strList.append(word + freq + '\n')
        join = ''.join(strList)
        return join
    else:
        raise Exception()
