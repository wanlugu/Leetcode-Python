class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bx = bin(x)
        by = bin(y)
        lenx = len(bx)
        leny = len(by)
        sum = 0
        if x<=y:
            for i in range(1,lenx-1):
                if bx[-i] != by[-i]:
                    sum = sum+1
            for j in range(2,leny-lenx+2):
                if by[j]== "1":
                    sum = sum+1
        else:
            for i in range(1,leny-1):
                if bx[-i] != by[-i]:
                    sum = sum+1
            for j in range(2,lenx-leny+2):
                if bx[j]== "1":
                    sum = sum+1
        return sum
            
        
        def hammingDistance1(self, x, y):
             """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')
