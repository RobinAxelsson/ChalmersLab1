import wordfreq
import sys

# example execution:
# $ python3 topmost.py eng_stopwords.txt examples/article1.txt 20
# $ py topmost.py eng_stopwords.txt examples/article1.txt 20


def run():
    filePathStop = sys.argv[1]
    filePathRead = sys.argv[2]
    topCount = int(sys.argv[3])

    with open(filePathStop, 'r', encoding="utf-8") as stopfile:
        stopText = stopfile.read()

    with open(filePathRead, encoding="utf-8") as readFile:
        readText = readFile.read()

    wordList = wordfreq.tokenize(readText)
    stopList = wordfreq.tokenize(stopText)
    wordDict = wordfreq.countWords(wordList, stopList)
    wordfreq.printTopMost(wordDict, topCount)

if __name__ == "__main__":
    run()