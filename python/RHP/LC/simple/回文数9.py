class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        number=0
        X=x
        while x>0:
            temp=x%10
            x=(x-temp)/10
            number=number*10+temp
        return number==X
if __name__ == '__main__':
    sol=Solution()
    print(sol.isPalindrome(121))