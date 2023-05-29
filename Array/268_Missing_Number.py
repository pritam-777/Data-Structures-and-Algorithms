def missingNumber(nums):
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                print(num)
                num_dict[num] = 1
                print(num_dict)
                
        for num in range(len(nums)+1):
            if num not in num_dict:
                return num
            

ls = [0,1,3]
print(missingNumber(ls))



#missing = len(nums)
#for i in range(len(nums)):
    #missing ^= i^nums[i]
#return missing ***