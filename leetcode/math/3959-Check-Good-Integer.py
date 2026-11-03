class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitsum=0
        squaresum=0
        for num in str(n):
            digitsum+=int(num)
            squaresum+=int(num)*int(num)
        if squaresum-digitsum>=50:
            return True
        else:
            return False
        