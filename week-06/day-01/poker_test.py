import unittest
from poker import *


class Poker_check(unittest.TestCase):

    def test_high_card_ace(self):
        a = Poker()
        self.assertEqual(a.hand_check(['2H', '3D', '5S', '9C', 'KD'],['2C', '3H', '4S', '8C', 'AH']), 'white wins')

    def test_find_highest_card(self):
        a = Poker()
        self.assertEqual(a.hand_check(['2H', '3D', '5S', '9C', 'KD'],['2C', '3H', '4S', '8C', '8S']), 'black wins')

    def test_find_pair(self):
        a = Poker()
        self.assertEqual(a.check_pair(['2H', '3D', '5S', '9C', '5D'],['2C', '3H', '4S', '7C', '8S']), 'black wins')

    def test_find_drill(self):
        a = Poker()
        self.assertEqual(a.check_pair(['2H', '3D', '5S', '5C', '5D'],['2C', '3H', '4S', '8C', '8S']), 'black wins')


    


if __name__ == '__main__':
    unittest.main()