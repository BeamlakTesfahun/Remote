class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pairsCounter = 0
        y = 0
        while y < len(nums):
            x = y + 1
            while x < len(nums):
                if nums[y] == nums[x] and y < x:
                    pairsCounter += 1
                x += 1
            y += 1
        return pairsCounter
        
