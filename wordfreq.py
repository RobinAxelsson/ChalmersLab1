
def tokenize(inputList: list):
    if not isinstance(inputList, list):
        raise Exception('You have to enter an list')
    if inputList == []:
         return []
    filtered = [line for line in inputList if line != '' and line.isspace() == False]
    if len(filtered) == 0:
        return []
    return [item for sublist in unpack(filtered) for item in sublist]

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