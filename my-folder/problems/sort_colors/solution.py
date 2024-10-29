class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr0 = 0
        ptr2 = len(nums) - 1
        i = 0
        while i <= ptr2:
            if nums[i] == 0:
                temp = nums.pop(i)
                nums.insert(ptr0, temp)
                ptr0 += 1
                i+= 1
            elif nums[i] == 2:
                temp = nums.pop(i)
                nums.insert(ptr2, temp)
                ptr2 -= 1
            else:
                i+= 1
        