class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start,end=0,1
        maxLength=0
        length=0
        for i in range(0,len(s)):
            end=i+1
            window=s[start:end]
            if s[i] in s[start:end-1]:
                while s[start] != s[i]:
                    start+=1
                start+=1
                length=end-start
            else:
                length=end-start
            maxLength=max(length,maxLength)
        return maxLength

    
            
                 

            



        