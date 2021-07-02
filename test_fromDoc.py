import unittest
import wordfreq

class TestFromDoc(unittest.TestCase):
    def test_tokenize_fromAssignmentDoc(self):
        document = ['"They had 16 rolls of duct tape, 2 bags of clothes pins,', '130 hampsters from the cancer labs down the hall, and', 'at least 500 pounds of grape jello and unknown amounts of chopped liver"', 'said the source on a recent Geraldo interview.']
        expect = ['"', 'they', 'had', '16', 'rolls', 'of', 'duct', 'tape', ',', '2', 'bags', 'of', 'clothes', 'pins', ',',
 '130', 'hampsters', 'from', 'the', 'cancer', 'labs', 'down', 'the', 'hall', ',', 'and', 'at', 'least',
 '500', 'pounds', 'of', 'grape', 'jello', 'and', 'unknown', 'amounts', 'of', 'chopped', 'liver', '"', 
 'said', 'the', 'source', 'on', 'a', 'recent', 'geraldo', 'interview', '.']
        actual = wordfreq.tokenize(document)
        self.assertEqual(expect, actual)