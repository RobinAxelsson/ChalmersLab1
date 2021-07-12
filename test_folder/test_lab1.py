import unittest
import wordfreq
import os
import test_folder.run_process as process
import sys
import io

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

    def test_tokenize_oneString(self):
        expect = ['python']
        actual = wordfreq.tokenize('python')
        self.assertEqual(expect, actual)

    def test_tokenize_stringText(self):
        expect = ['python', 'python', 'java']
        actual = wordfreq.tokenize('python    python  java ')
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

    # run_process.py #
    def test_runner_expect_same(self):
        expect = 'test_folder/run_args.py arg1 arg2\n'
        actual = process.run('py test_folder/run_args.py arg1 arg2')
        self.assertEqual(expect, actual)

    def test_runfolder_expect_lab1(self):
        expect = 'lab1'
        actual = os.getcwd().split('\\')[-1]
        self.assertEqual(expect, actual)
    
    def test_runfolder_process(self):
        expect = 'lab1\n'
        actual = process.run('py test_folder/run_path.py')
        self.assertEqual(expect, actual)

    def test_runhello_process(self):
        expect = 'Hello World\n'
        actual = process.run('py test_folder/run_hello.py test_folder/hello.txt')
        self.assertEqual(expect, actual)

    # fake print to test topmost #

    def fakePrint(text):
        saved = sys.stdout
        sys.stdout = io.StringIO()
        print(text)
        out = sys.stdout.getvalue()
        sys.stdout = saved
        return out

    def fakePrintTopMost(freq,n):
        saved = sys.stdout
        sys.stdout = io.StringIO()
        wordfreq.printTopMost(freq,n)
        out = sys.stdout.getvalue()
        sys.stdout = saved
        return out
    def test_fakePrintTopMost(self):
        expect = 'Hello World\n'
        actual = TestWordfreq.fakePrint('Hello World')
        self.assertEqual(expect, actual)
    
    ## printTopMost ##

    def test_printTopMost_empty_dict(self):
        expect = ""
        actual = TestWordfreq.fakePrintTopMost({}, 10)
        self.assertEqual(expect, actual)
    
    def test_printTopMost_Zero_words(self):
        expect = ""
        actual = TestWordfreq.fakePrintTopMost({"horror": 5, "happiness": 15},0)
        self.assertEqual(expect, actual)

    def test_printTopMost_C_python_haskell_java(self):
        expect = "python                  5\nC                       3\nhaskell                 2\n"
        actual = TestWordfreq.fakePrintTopMost({"C": 3, "python": 5, "haskell": 2, "java": 1},3)
        self.assertEqual(expect, actual)

    ## run printTopMost.py with args ##

    def test_py_printTopMost_3python(self):
        expect = "python                  3\n"
        actual = process.run('py topmost.py eng_stopwords.txt test_folder/test_example1.txt 1')
        self.assertEqual(expect, actual)

    def test_py_printTopMost_ask3words(self):
        expect = "python                  3\n"
        actual = process.run('py topmost.py eng_stopwords.txt test_folder/test_example1.txt 3')
        self.assertEqual(expect, actual)

    # def test_py_printTopMost_localhost8000(self):
    ## startup server with command python3 -m http.server
    #     expect = "python                  3\n"
    #     actual = process.run('py topmost.py eng_stopwords.txt http://localhost:8000/test_folder/test_example1.txt 3')
    #     self.assertEqual(expect, actual)