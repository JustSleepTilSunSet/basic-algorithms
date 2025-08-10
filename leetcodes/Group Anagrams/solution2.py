"""
The solution failed in special case.
total of the "duh" is 33 that equals "ill".
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Create result
        result_board = {}
        for content in strs:
            alpha_dictionary = {
                "a":0,
                "b":0,
                "c":0,
                "d":0,
                "e":0,
                "f":0,
                "g":0,
                "h":0,
                "i":0,
                "j":0,
                "k":0,
                "l":0,
                "m":0,
                "n":0,
                "o":0,
                "p":0,
                "q":0,
                "r":0,
                "s":0,
                "t":0,
                "u":0,
                "v":0,
                "w":0,
                "x":0,
                "y":0,
                "z":0,
                }
            # Freqency.
            for word in content:
                alpha_dictionary[word] = alpha_dictionary[word]+1
            print(alpha_dictionary)
            # Generate key string.
            result_key = "" 
            for key in alpha_dictionary.keys():
                if alpha_dictionary[key] == 0:
                    continue
                result_key = result_key + (key+str(alpha_dictionary[key]))
            if result_board.get(result_key) is None:
                result_board[result_key] = [content]
            else:
                result_board[result_key].append(content)
        print(result_board)
        return result_board.values()
print(Solution().groupAnagrams(strs=["eat","ate"]))
