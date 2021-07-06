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
        stopWords: list[str] = [word for word in stopfile.readlines()]

    with open(filePathRead, encoding="utf-8") as readFile:
        readWords: list[str] = [word for word in readFile.readlines()]

    wordList = wordfreq.tokenize(readWords)
    stopList = wordfreq.tokenize(stopWords)
    wordDict = wordfreq.countWords(wordList, stopList)
    wordfreq.printTopMost(wordDict, topCount)

if __name__ == "__main__":
    run()