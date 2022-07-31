from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alien_order(self, words: List[str]) -> str:
        # Write your code here

        d = {i: set() for w in words for i in w}

        def letter_mapping(s1, s2):

            min_length = min(len(s1), len(s2))

            if len(s1) > len(s2) and s1[:min_length] == s2[:min_length]:
                return False

            for i in range(min_length):
                if s1[i] != s2[i]:
                    d[s1[i]].add(s2[i])
                    break

            return True


        for i in range(len(words)-1):
            if not letter_mapping(words[i], words[i+1]):
                return ""

        
        res = []
        processed = set()
        curr_path = set()
        no_order = []

        def helper(letter):
            if letter in curr_path:
                return False

            if letter in processed:
                return True

            curr_path.add(letter)

            for nei in d[letter]:
                if not helper(nei):
                    return False

            curr_path.remove(letter)
            processed.add(letter)
            res.append(letter)

            return True


        for c in d:                             # iterates through all the keys in d
            if not d[c]:                        # if the value for the current char is empty, append in no_order list
                no_order.append(c)
            else:
                if not helper(c):
                    return ""

        no_order.sort()
        res.reverse()

        p1, p2 = 0,0
        result_string = ""
        result_set = set(res)

        while p1 < len(no_order) and p2 < len(res):
            if no_order[p1] in result_set:
                p1+= 1
                continue 
            
            if no_order[p1] < res[p2]:
                result_string += no_order[p1]
                p1 += 1

            else:
                result_string += res[p2]
                p2 += 1

        while p1 < len(no_order):
            result_string += no_order[p1]
            p1 += 1

        while p2 < len(res):
            result_string += res[p2]
            p2 += 1
        

        return result_string

    # TC: number of letters in the input ( not words ) since we are visiting each letter once ( due to the processed set, 
    # we do not process the same letter again). Hence total TC: O(num_letters_in_input)

    # SC: O(num_letters_in_input) because the dictionary, recursion and all other DS can have a max of total letters in the input.