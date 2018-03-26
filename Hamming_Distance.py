class Solution(object):
    """docstring for ClassName"""
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count=0
        mid_var=x^y
        while mid_var!=0:
            count+=mid_var & 1
            mid_var>>=1
        return count