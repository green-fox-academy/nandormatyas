import unittest
from nandi_work import *

class TestApple(unittest.TestCase):
    def test_same_string(self):
        apple = Apple()
        self.assertEqual(apple.get_apple(apple), apple)

summa = Summa()
class TestSumma(unittest.TestCase):

    def test_sum_of_empty(self):
        self.assertEqual(summa.sum_numbers([]), 0)
    def test_with_3_numbers(self):
        self.assertEqual(summa.sum_numbers([4,5,6]), 15)
    def test_one_element(self):
        self.assertEqual(summa.sum_numbers([2]), 2)
    def test_null(self):
        self.assertEqual(summa.sum_numbers([0]), 0)

anagram = Anagram()
class TestAnagram(unittest.TestCase):
    def test_for_anagram(self):
        self.assertEqual(anagram.anagram('gorog', 'rogog'), True)
    def test_for_not_anagram(self):
        self.assertEqual(anagram.anagram('asdasd', 'dasqwe'), False)

letter_counter = LetterCounter()
class TestLetterCounter(unittest.TestCase):
    def test_one_character(self):
        self.assertEqual(letter_counter.count_letters('a'), {'a': 1})
    def test_multiple_characters(self):
        self.assertEqual(letter_counter.count_letters('asd'), {'a': 1, 's': 1, 'd': 1})
    def test_more_occurence(self):
        self.assertEqual(letter_counter.count_letters('aaqweq'), {'a': 2, 'q': 2, 'w':1, 'e':1})
    def test_no_character(self):
        self.assertEqual(letter_counter.count_letters(''), {})

fibo = Fibonacci()
class TestFibonacci(unittest.TestCase):
    def test_give_zero(self):
        self.assertEqual(fibo.fibonacci_index(0), 0)
    def test_give_one(self):
        self.assertEqual(fibo.fibonacci_index(1), 0)
    def test_give_two(self):
        self.assertEqual(fibo.fibonacci_index(2), 1)
    def test_give_nine(self):
        self.assertEqual(fibo.fibonacci_index(9), 21)

if __name__ == '__main__':
    unittest.main()