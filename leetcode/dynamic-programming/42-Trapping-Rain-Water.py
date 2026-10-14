class Solution:
    def prefix(self,height,n):
        prefixmax=[0]*n
        prefixmax[0]=height[0]
        for i in range(1,n):
            prefixmax[i]=max(prefixmax[i-1],height[i])
        return prefixmax
    def suffix(self,height,n):
        suffixmax=[0]*n
        suffixmax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            suffixmax[i]=max(suffixmax[i+1],height[i])
        return suffixmax

    def trap(self, height: list[int]) -> int:
        n=len(height)
        total=0
        leftmax=self.prefix(height,n)
        rightmax=self.suffix(height,n)
        for i in range(n):
            if (height[i]<leftmax[i] and height[i]<rightmax[i]):
                total+=(min(leftmax[i],rightmax[i])-height[i])
        return total
        