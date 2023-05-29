class Solution:
    def findDuplicate(self, nums) -> int:
        HashSet = set()
        for i in nums:
            if i in HashSet:
                return i
            HashSet.add(i)
        return -1