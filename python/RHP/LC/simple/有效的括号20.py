from collections import deque


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        queue=list()
        for ch in s:
            if len(queue)==0 and ( ch==']' or ch=='}' or ch==')'):
                return False
            if ch in ['(','{','[']:
                queue.append(ch)
            else:
                if ch ==']' and queue[-1]=='[':
                    queue.pop()
                elif ch==')'  and queue[-1]=='(':
                    queue.pop()
                elif ch=='}' and queue[-1]=='{':
                    queue.pop()
                else:
                    return False

        return len(queue)==0

if __name__ == '__main__':
    sol=Solution()
    s='(){}}{'
    print(sol.isValid(s))
    mylist=list()
    mylist.append('1')
    mylist.append('2')
    mylist.append('3')
    print(mylist.pop())
    print(mylist)

