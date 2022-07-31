from typing import (
    List,
)

class Solution:
    """
    @param s: the given string
    @return: all the palindromic permutations (without duplicates) of it
             we will sort your return value in output
    """
    def generate_palindromes(self, s: str) -> List[str]:
        # write your code here

        d = collections.Counter(s)
        odd = 0
        res = []
        odd_char = ""

        for key, val in d.items():
            if val % 2:
                odd_char += key
                odd += 1

        if odd > 1:
            return res 

        def helper(string):

            if len(string) == len(s):
                res.append(string)
                return

            for char in d.keys(): # n/ 2 keys

                if d[char] > 0:
                    d[char] -= 2
                    helper(char + string + char)
                    d[char] += 2

        
        if odd:
            d[odd_char] -= 1
            helper(odd_char)

        else:
            helper("")

        return res

    # TC: O(n^2) where n is the number of charaters in the string, SC: O(n) where n because max depth of recursion = length of string.