class Apple():

    def get_apple(self, string_input):
        return string_input

class Summa():

    def sum_numbers(self, numbers):
        summa = 0
        for number in numbers:
            summa += number
        return summa

class Anagram():
    def anagram(self, one_string, two_string):
        one_string = one_string.replace(" ", "").lower()
        two_string = two_string.replace(" ", "").lower()
        list1 = list()
        list2 = list()
        for i in one_string:
            list1.append(i)
        for j in two_string:
            list2.append(j)
        list1 = sorted(list1)
        list2 = sorted(list2)
        if list1 == list2:
            return True
        else:
            return False

class LetterCounter():
    def count_letters(self, string):
        letters = dict()
        for letter in string:
            if letter in letters:
                letters[letter] +=1
            else:
                letters[letter] = 1
        return letters

class Fibonacci():
    def fibonacci_index(self, index_number):
        if index_number == 0:
            return 0
        elif index_number == 1:
            return 0
        elif index_number == 2:
            return 1
        else:
            return self.fibonacci_index(index_number - 1) + self.fibonacci_index(index_number - 2)





