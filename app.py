import wordfreq
import sys

# example execution:
# $ python3 topmost.py eng_stopwords.txt examples/article1.txt 20
# $ py topmost.py eng_stopwords.txt examples/article1.txt 20
def run():
    # for arg in sys.argv:
    #     print(arg)
    filePathStop = 'eng_stopwords.txt'
    filePathRead = 'examples/article4.txt'
    topCount = 20

    with open(filePathStop, 'r', encoding="utf-8") as f:
        file_contents = f.read()

    stopFile = open(filePathStop, encoding="utf-8")
    stopWords: list[str] = [word for word in stopFile]
    stopFile.close()

    readFile = open(filePathRead, encoding="utf-8")
    readWords: list[str] = [word for word in readFile]
    readFile.close()

    wordList = wordfreq.tokenize(readWords)
    wordDict = wordfreq.countWords(wordList, stopWords)
    printable = wordfreq.printTopMost(wordDict, topCount)
    print(printable)