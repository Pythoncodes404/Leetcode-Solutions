class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i

        return res


    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here

        res = []
        i = 0
        num = ""

        while i < len(str):

            if str[i] == "#":

                eow = int(num) + i + 1
                num = ""
                res.append(str[i+1 : eow])
                i = eow

            else:
                num += str[i]
                i += 1

        return res