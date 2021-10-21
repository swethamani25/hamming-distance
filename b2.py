class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
