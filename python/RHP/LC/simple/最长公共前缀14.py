class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        perfix,count=strs[0],len(strs)
        for i in range(1,count):
            perfix=self.lc(perfix,strs[i])
            if not perfix:
                break
        return perfix
    def lc(self,str1,str2):
        index=0
        length=min(len(str1),len(str2))
        while index<length:
            if str1[index]==str2[index]:
                index+=1
            else:break
        return str2[:index]


if __name__ == '__main__':
    sol=Solution()
    mylist=['aab','aabcc','aacc']
    print(sol.longestCommonPrefix(mylist))