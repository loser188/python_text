class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index=1
        i=0
        while i < len(nums)-1:
            if nums[i]==nums[i+1]:
                i=i+1
                nums.pop(i)
                continue
            else:
                nums[index]=nums[i] # 为什么这一步不生效？？？
                print(nums[index],index)
                index+=1
                i=i+1
            print(nums)
        return index
if __name__ == '__main__':
    mylist=[1,1,2,3,4,5,5,6]
    sol=Solution()
    print(sol.removeDuplicates(mylist))


