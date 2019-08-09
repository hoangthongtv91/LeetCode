import sys


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2147483647 or x < -2147483648:
            return 0
        y = x
        rev = 0
        if y < 0:
            y = -y
        while y > 0:
            rev = y % 10 + rev * 10
            y //= 10

        if x < 0:
            return -rev
        else:
            return rev


    print(sys.maxsize)
    print(reverse("a", -1563847412))