def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = 0
        counter = 0
        for i in nums:
                if counter==0:
                        candidate=i
                if candidate==i:
                        counter+=1
                else:
                    counter -= 1
        return candidate




ls=[3,2,3]
print(majorityElement(ls))