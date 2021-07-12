import wordfreq
import sys
import urllib.request

# example exec:
# $ py topmost.py eng_stopwords.txt examples/article1.txt 20
# $ py topmost.py eng_stopwords.txt http://info.cern.ch/hypertext/WWW/TheProject.html 20

def run():
    urlSkipWords = sys.argv[1]
    urlRead = sys.argv[2]
    topCount = int(sys.argv[3])

    if 'https://' in urlSkipWords or 'http://' in urlSkipWords:
        response = urllib.request.urlopen(urlSkipWords)
        stopText = response.read().decode("utf8")
    else:
        with open(urlSkipWords, 'r', encoding="utf-8") as stopfile:
            stopText = stopfile.read()

    if 'https://' in urlRead or 'http://' in urlRead:
        response = urllib.request.urlopen(urlRead)
        readText = response.read().decode("utf8")
    else: 
        with open(urlRead, encoding="utf-8") as readFile:
            readText = readFile.read()

    wordList = wordfreq.tokenize(readText)
    stopList = wordfreq.tokenize(stopText)
    wordDict = wordfreq.countWords(wordList, stopList)
    wordfreq.printTopMost(wordDict, topCount)

if __name__ == "__main__":
    run()