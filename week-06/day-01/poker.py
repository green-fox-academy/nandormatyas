class Poker():
    def __init__(self):
        self.rule_list = ['2' , '3','4', '5', '6', '7', '8' , '9', 'T', 'J', 'Q', 'K', 'A']

    def hand_check(self, hand_one, hand_two):
        highest_one = 0
        highest_two = 0
        for card in hand_one:
            if self.rule_list.index(card[0]) > highest_one:
                highest_one = self.rule_list.index(card[0])
        for card in hand_two:
            if self.rule_list.index(card[0]) > highest_two:
                highest_two = self.rule_list.index(card[0])
        if highest_one > highest_two:
            return 'black wins'
        return 'white wins'
    def check_pair(self, hand_one, hand_two):
        test_pairs = []
        count_one = 1
        count_two = 1
        for card in hand_one:
            if card[0] not in test_pairs:
                test_pairs.append(card[0])   
            else:
                count_one +=1
        test_pairs1 = []
        for card in hand_two:
            if card[0] not in test_pairs1:
                test_pairs1.append(card[0])   
            else:
                count_two +=1
        if count_one > count_two:
            return 'black wins'
        return 'white wins' 

         