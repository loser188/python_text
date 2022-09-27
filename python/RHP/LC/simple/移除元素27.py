class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        index=0
        while i < len(nums):
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
                i = i + 1
            else:
                i=i+1
                continue
        return index
if __name__ == '__main__':
 nums=[1,2,3,3,4,4,4,5,5,6]
 sol=Solution()
 print(sol.removeElement(nums, 4))