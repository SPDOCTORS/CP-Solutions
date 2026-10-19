class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        row=len(matrix)
        cols=len(matrix[0])
        heights=[0]*cols
        max_area=0
        for i in range(row):
            for j in range(cols):
                if matrix[i][j]=="1":
                    heights[j]+=1
                else:
                    heights[j]=0
            stack=[]
            for j in range(cols):
                while stack and heights[stack[-1]]>heights[j]:
                    idx=stack.pop()
                    h=heights[idx]
                    if stack:
                        left=stack[-1]
                    else:
                        left=-1
                    width=j-left-1
                    area=h*width
                    max_area=max(max_area,area)
                stack.append(j)
            while stack:
                idx=stack.pop()
                h=heights[idx]
                if stack:
                    left=stack[-1]
                else:
                    left=-1
                width=cols-left-1
                area=h*width
                max_area=max(max_area,area)
        return max_area
        