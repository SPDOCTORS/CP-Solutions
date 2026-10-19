class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n=len(heights)
        max_area=0
        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                idx=stack.pop()
                h=heights[idx]
                if stack:
                    left=stack[-1]
                else:
                    left=-1
                width=i-left-1
                area=h*width
                max_area=max(max_area,area)
            stack.append(i)
        while stack:
            idx=stack.pop()
            h=heights[idx]
            if stack:
                left=stack[-1]
            else:
                left=-1
            width=n-left-1
            area=h*width
            max_area=max(max_area,area)
        return max_area    