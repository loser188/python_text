class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)
        while left<=right:
            mid=(right+left)//2
            if nums[mid]==target or (nums[mid]<target and nums[mid+1]>target):
                return mid+1
            elif nums[mid]<target and nums[mid+1]<target:
                left=mid+1
            else: right=mid-1
        return -1
if __name__ == '__main__':
    nums=[1,3,4,5,7,8,9,9]
    sol=Solution()
    print(sol.searchInsert(nums, 1))