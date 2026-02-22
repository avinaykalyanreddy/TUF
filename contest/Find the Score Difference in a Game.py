"""
You are given an integer array nums, where nums[i] represents the points scored in the ith game.

There are exactly two players. Initially, the first player is active and the second player is inactive.

The following rules apply sequentially for each game i:

If nums[i] is odd, the active and inactive players swap roles.
In every 6th game (that is, game indices 5, 11, 17, ...), the active and inactive players swap roles.
The active player plays the ith game and gains nums[i] points.
Return the score difference, defined as the first player's total score minus the second player's total score.
"""


class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        player1 = 0
        player2 = 0

        x = True
        y = False

        low = 0

        for i in range(len(nums)):

            if nums[i] % 2 == 1:

                if x:

                    y = True
                    x = False

                else:

                    x = True
                    y = False

            if i - low == 5:

                if x:

                    y = True
                    x = False

                else:

                    x = True
                    y = False

                low = i + 1

            if x:
                player1 += nums[i]

            else:

                player2 += nums[i]

        return (player1 - player2)



