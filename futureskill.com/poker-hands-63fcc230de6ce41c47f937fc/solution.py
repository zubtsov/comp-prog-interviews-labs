class Solution:
    rank_dict = {"A": 14, "K": 13, "Q": 12, "J": 11,
                 "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

    @staticmethod
    def has_different_suit(hand):
        return len(set(map(lambda s: s[1], hand))) > 1

    def __init__(self, api):
        self.api = api

    def level_1_is_flush(self, hand):
        return len(set(map(lambda s: s[1], hand))) == 1

    def level_2_is_straight(self, hand):
        sorted_ranks = list(sorted(map(lambda s: Solution.rank_dict[s[0]], hand)))
        ace = Solution.rank_dict['A']

        if ace in sorted_ranks:
            sorted_ranks.remove(ace)
            sequential_rank = sorted_ranks[-1] - sorted_ranks[0] == 3 and (
                    sorted_ranks[0] == 2 or sorted_ranks[-1] == 13)
        else:
            sequential_rank = sorted_ranks[-1] - sorted_ranks[0] == 4 and len(set(sorted_ranks)) == 5

        return Solution.has_different_suit(hand) and sequential_rank

    def level_3_is_royal_straight_flush(self, hand):
        has_same_suit = not Solution.has_different_suit(hand)

        sorted_ranks = list(sorted(map(lambda s: Solution.rank_dict[s[0]], hand)))

        return has_same_suit and (sorted_ranks[-1] == 14 and sorted_ranks[0] == 10) and len(set(sorted_ranks)) == 5
