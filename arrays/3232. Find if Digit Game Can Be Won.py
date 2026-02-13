class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:

        single = 0
        double = 0

        for i in nums:

            if len(str(i)) > 1:

                double += i

            else:

                single += i

        if single > double or double > single:
            return True

        return False
