class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result=0
        x_str=str(x)[::-1]
        if x_str[-1]=='-':
            result=-1*int(x_str[0:len(x_str)-1])
        else:
            result=int(x_str[0:len(x_str)])
        return result*(abs(result)<2**31)
       
        
        
        