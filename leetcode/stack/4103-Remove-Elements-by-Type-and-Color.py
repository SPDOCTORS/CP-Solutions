class Solution:
    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
        stack=[]
        n=len(types)
        for i in range(n):
            t=types[i]
            c=colors[i]
            if stack and stack[-1][0] == t and stack[-1][1] == c:
                stack[-1][2]+=1
            else:
                stack.append([t,c,1])
            if stack[-1][2]==groupSize[t]:
                stack.pop()
        return True if len(stack)==0 else False
