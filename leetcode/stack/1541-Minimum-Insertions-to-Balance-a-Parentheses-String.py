class Solution:
    def minInsertions(self, s: str) -> int:
        i=0
        left_count=0
        require=0
        while i<len(s):
            if s[i]=="(":
                left_count+=1
                i+=1
            else:
                if left_count>0:
                    left_count-=1
                else:
                    require+=1
                if i<len(s)-1 and s[i+1]==")":
                    i+=2
                else:
                    require+=1
                    i+=1
        require+=left_count*2
        return require

        