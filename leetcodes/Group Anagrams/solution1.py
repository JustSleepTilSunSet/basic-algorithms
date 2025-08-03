class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Create word dictionary.
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
        alpha_index = 1
        for key in alpha_dictionary.keys():
            alpha_dictionary[key] = alpha_index 
            alpha_index = alpha_index + 1

        # Create result
        result = {}
        for content in strs:
            content_value = 0
            for word in content:
                content_value = content_value + alpha_dictionary[word]
            if result.get(str(content_value)) is None:
                result[str(content_value)] = [str(content)]
            else:
                result[str(content_value)].append(str(content))
        print(result.values())
        return result.values()
