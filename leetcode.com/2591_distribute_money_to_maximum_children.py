class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        money_left_after_min_donation = money - children  # give each child 1 dollar
        max_donation_children = money_left_after_min_donation // 7

        if max_donation_children > children:
            return children - 1
        elif max_donation_children == children and money_left_after_min_donation % 7 == 0:
            return max_donation_children
        elif max_donation_children == children:
            return max_donation_children - 1
        elif max_donation_children < children:
            if money_left_after_min_donation % 7 == 3 and (children - max_donation_children) == 1:
                return max_donation_children - 1
            else:
                return max_donation_children


if __name__ == '__main__':
    s = Solution()

    tcs = [
        (23, 2, 1),
        (11, 2, 1),
        (5, 2, 0),
        (11, 3, 1),
        (20, 3, 1),
        (16, 2, 2),
        (17, 2, 1),
    ]

    for money, children, expected in tcs:
        actual = s.distMoney(money, children)
        print(actual)
        assert actual == expected
