class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}

        index = 0
        # Traverse nums.
        for num in nums:
            pair = target - num
            # Get pair.
            if lookup.get(pair) is not None:
                return [lookup[pair],index]

            # Save to map.
            lookup[num]=index
            index+=1

        return []