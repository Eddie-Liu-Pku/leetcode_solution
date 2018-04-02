class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_num={}
        #有两个相同元素的情况下，必须仔细考虑
        for i in range(len(nums)):
            if target-nums[i] in dict_num:
                return [dict_num[target-nums[i]],i]
            dict_num[nums[i]]=i