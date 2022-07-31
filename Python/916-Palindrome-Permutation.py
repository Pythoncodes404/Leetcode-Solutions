class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def can_permute_palindrome(self, s: str) -> bool:
        # write your code here

        d = collections.Counter(s)

        odd = 0

        for i in d.values():

            if i% 2:
                odd += 1


        return True if odd < 2 else False