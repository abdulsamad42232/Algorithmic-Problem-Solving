class Solution(object):
    def twoSum(self, nums, target):
        my_hash={}
        for index,item in enumerate(nums):
            res = target-item
            if res in my_hash:
                return([my_hash[res],index])
            my_hash[item]=index