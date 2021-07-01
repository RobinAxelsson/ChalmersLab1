
def tokenize(inputList: list):
    if not isinstance(inputList, list):
        raise Exception('You have to enter an list')
    if inputList == []:
         return []
    filtered = [line for line in inputList if line != '' and line.isspace() == False]
    if len(filtered) == 0:
        return []
    split = [item for sublist in unpack(filtered) for item in sublist]
    sepparated = []
    for word in split:
        sepparated.extend(sepparate(word, ['!', 'th']))
    return sepparated

def sepparate(word: str, seps: list[str]):
    seppareted = []
    stripWord = word
    for sep in seps:
        if sep in word:
            seppareted.append(sep)
            stripWord.strip(sep)
    seppareted.append(stripWord)
    return seppareted


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