import unittest
import wordfreq
import test_folder.run_process as process
class TestWordfreq(unittest.TestCase):
    #### testing.typeSplit ####
    def test_typeSplit(self):
        expect = ['!', ',', '?', 'aaa']
        actual = wordfreq.typeSplit("!,?aaa")
        self.assertEqual(expect, actual)

    def test_typeSplit_14th(self):
        expect = ["15","th"]
        actual = wordfreq.typeSplit("15th")
        self.assertEqual(expect, actual)

    def test_typeSplit_stacked(self):
        expect = ["th", "!", "!", "!"]
        actual = wordfreq.typeSplit("th!!!")
        self.assertEqual(expect, actual)

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

    def test_tokenize_fromAssignmentDoc(self):
        document = ['"They had 16 rolls of duct tape, 2 bags of clothes pins,', '130 hampsters from the cancer labs down the hall, and', 'at least 500 pounds of grape jello and unknown amounts of chopped liver"', 'said the source on a recent Geraldo interview.']
        expect = ['"', 'they', 'had', '16', 'rolls', 'of', 'duct', 'tape', ',', '2', 'bags', 'of', 'clothes', 'pins', ',',
 '130', 'hampsters', 'from', 'the', 'cancer', 'labs', 'down', 'the', 'hall', ',', 'and', 'at', 'least',
 '500', 'pounds', 'of', 'grape', 'jello', 'and', 'unknown', 'amounts', 'of', 'chopped', 'liver', '"', 
 'said', 'the', 'source', 'on', 'a', 'recent', 'geraldo', 'interview', '.']
        actual = wordfreq.tokenize(document)
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
        
    def test_printTopMost_Top3(self):
        expect = "python                  5\nC                       3\nhaskell                 2\n"
        actual = wordfreq.printTopMost({"C": 3, "python": 5, "haskell": 2, "java": 1},3)
        self.assertEqual(expect, actual)

    # run_process.py #
    def test_runner_expect_same(self):
        expected = 'test_folder/testrun.py arg1 arg2\n'
        actual = process.run('py test_folder/testrun.py arg1 arg2')
        self.assertEqual(expected, actual)
