"""
You are given a string s consisting of lowercase English letters and the special characters: *, #, and %.

Build a new string result by processing s according to the following rules from left to right:

If the letter is a lowercase English letter append it to result.
A '*' removes the last character from result, if it exists.
A '#' duplicates the current result and appends it to itself.
A '%' reverses the current result.
Return the final string result after processing all characters in s.
"""
class Solution:
    def processStr(self, s: str) -> str:
        result = []

        def remove():

            if not result:

                return

            result.pop()

        def duplicate(result):

            if not result:

                return

            l = len(result)

            for i in range(l):

                result.append(result[i])

        def reverse(result):

            if not result:

                return

            low = 0
            high = len(result)-1

            while low < high:

                result[low], result[high] = result[high],result[low]

                low += 1
                high -= 1

        for i in s:

            if i == '*':

                remove()

            elif i == '#':

                duplicate(result)

            elif i == '%':

                reverse(result)

            else:

                result.append(i)

        return "".join(result)