class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts={}
        l=0
        max_length=0
        for r in range(len(s)):
            if s[r] in counts:
                counts[s[r]]+=1
            else:
                counts[s[r]]=1
            max_count=max(counts.values())
            length=r-l+1
            if length - max_count > k:
                counts[s[l]]-=1
                l+=1
                continue
            max_length = max(length,max_length)
        return max_length
            

            

            



        