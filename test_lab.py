import unittest
import wordfreq

class TestWordfreq(unittest.TestCase):

    # wordfreq.tokenize
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
        actual = wordfreq.tokenize("   ")
        self.assertEqual(expect, actual)

    def test_tokenize_sentenceStringToLower(self):
        expect = ["this","is","a","simple","sentence"]
        actual = wordfreq.tokenize(["This is a simple sentence"])
        self.assertEqual(expect, actual)

    # ["I told you!"], ["i","told","you","!"]
    # ["The 10 little chicks"], ["the","10","little","chicks"]
    # ["15th anniversary"], ["15","th","anniversary"]
    # ["He is in the room, she said."], ["he","is","in","the","room",",","she","said","."]

    # wordfreq.countWords

    # ([],[]), {}
    # (["clean","water"],[]), {"clean":1,"water":1}
    # (["clean","water","is","drinkable","water"],[]), {"clean":1,"water":2,"is":1,"drinkable":1}
    # (["clean","water","is","drinkable","water"],["is"]), {"clean":1,"water":2,"drinkable":1}

    # wordfreq.printTopMost

    # ({},10),""
    # ({"horror": 5, "happiness": 15},0),""
    # ({"C": 3, "python": 5, "haskell": 2, "java": 1},3),"python                  5\nC                       3\nhaskell                 2\n"
