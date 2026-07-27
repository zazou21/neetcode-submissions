class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts={}
        count_window={}
        match=0
        res=[-1,-1]
        for char in t:
            counts[char]=1 + counts.get(char,0)
        start=0
        min_str=""
        min_length=float('inf')
        flag_first=True
        for r in range(len(s)):
            char=s[r]
            count_window[char]=1+count_window.get(char,0)
            if char in counts and count_window[char] == counts[char]:
                match+=1
          
            while match == len(counts):
                if min_length>r-start+1:
                    min_length=r-start+1
                    min_str=s[start:r+1]
                count_window[s[start]]-=1
                if s[start] in counts and count_window[s[start]] == counts[s[start]]-1:
                    match-=1
                start+=1
           
        return min_str


            
            


             
        