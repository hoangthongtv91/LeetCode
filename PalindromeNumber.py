class Solution(object):
    def isPalindrome(self, x):
        s1 = str(x)
        s2 = str(x)[::-1]
        if s1 == s2:
            return True
        else:
            return False