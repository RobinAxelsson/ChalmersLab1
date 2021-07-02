import unittest
import wordfreq

class TestWordfreq(unittest.TestCase):
    #### testing.symbols ####
    
    #### wordfreq.tokenize ####
    def test_tokenize_emptyArray(self):
        expect = []
        actual = wordfreq.tokenize([])
        self.assertEqual(expect, actual)
    
    def test_tokenize_EmptyString(self):
        expect = []
        actual = wordfreq.tokenize([""])
        self.assertEqual(expect, actual)

    def test_tokenize_blankSpaces(self):
        expect = []
        actual = wordfreq.tokenize(["   "])
        self.assertEqual(expect, actual)

    def test_tokenize_sentenceStringToLower(self):
        expect = ["this","is","a","simple","sentence"]
        actual = wordfreq.tokenize(["This is a simple sentence"])
        self.assertEqual(expect, actual)

    def test_tokenize_specialChar(self):
        expect = ["i","told","you","!"]
        actual = wordfreq.tokenize(["I told you!"])
        self.assertEqual(expect, actual)
    
    def test_tokenize_twoSentence(self):
        expect = ["the","10","little","chicks"]
        actual = wordfreq.tokenize(["The 10 little chicks"])
        self.assertEqual(expect, actual)
    
    def test_tokenize_th(self):
        expect = ["15","th","anniversary"]
        actual = wordfreq.tokenize(["15th anniversary"])
        self.assertEqual(expect, actual)

    def test_tokenize_th(self):
        expect = ["he","is","in","the","room",",","she","said","."]
        actual = wordfreq.tokenize(["He is in the room, she said."])
        self.assertEqual(expect, actual)
    
    def test_tokenize_word_space(self):
        expect = ["java", "java"]
        actual = wordfreq.tokenize(["   java    java    "])
        self.assertEqual(expect, actual)

    #### wordfreq.separateEnd ####
    def test_separateEnd_14th(self):
        expect = ["15","th"]
        actual = wordfreq.separateEnd("15th", ["th"])
        self.assertEqual(expect, actual)
    
    def test_separateEnd_the(self):
        expect = ["the"]
        actual = wordfreq.separateEnd("the", ["th"])
        self.assertEqual(expect, actual)

    def test_separateEnd_gather(self):
        expect = ["gather"]
        actual = wordfreq.separateEnd("gather", ["th"])
        self.assertEqual(expect, actual)

    #### wordfreq.separateMarks ####
    def test_separateMarks_stacked(self):
        expect = ["th", "!", "!", "!"]
        actual = wordfreq.separateMarks("th!!!", ["!"])
        self.assertEqual(expect, actual)

    #### wordfreq.countWords ####
    def test_countWords_emptyList(self):
        expect = {}
        actual = wordfreq.countWords([], [])
        self.assertEqual(expect, actual)

    def test_countWords_clean_water(self):
        expect = {"clean":1,"water":1}
        actual = wordfreq.countWords(["clean","water"],[])
        self.assertEqual(expect, actual)

    def test_countWords_twoArray(self):
        expect = {"clean":1,"water":2,"drinkable":1}
        actual = wordfreq.countWords(["clean","water","is","drinkable","water"],["is"])
        self.assertEqual(expect, actual)
    
    def test_countWords_twoWater(self):
        expect = {"clean":1,"water":2,"is":1,"drinkable":1}
        actual = wordfreq.countWords(["clean","water","is","drinkable","water"],[])
        self.assertEqual(expect, actual)

    def test_countWords_twoWater_removeis(self):
        expect = {"clean":1,"water":2,"drinkable":1}
        actual = wordfreq.countWords(["clean","water","is","drinkable","water"],["is"])
        self.assertEqual(expect, actual)
    
    def test_countWords_one(self):
        expect = {"java":1}
        actual = wordfreq.countWords(["java"],[])
        self.assertEqual(expect, actual)

    # wordfreq.printTopMost

    def test_printTopMost_empty_dict(self):
        expect = {}
        actual = wordfreq.printTopMost({}, 10)
        self.assertEqual(expect, actual)
        
    def test_printTopMost_Top0(self):
        expect = ""
        actual = wordfreq.printTopMost({"horror": 5, "happiness": 15},0)
        self.assertEqual(expect, actual)
    
    # def test_printTopMost_Top3(self):
    #     expect = {"java": 1}
    #     words = wordfreq.tokenize(["java       "])
    #     wordDict = wordfreq.countWords(words, [])
    #     actual = wordfreq.printTopMost(wordDict, 3)
    #     self.assertEqual(expect, actual)
    # This one seems strange, need to check docs.
    # ({"C": 3, "python": 5, "haskell": 2, "java": 1},3),"python                  5\nC                       3\nhaskell                 2\n"
