class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sptr=fptr=0
        while True:
            sptr=nums[sptr]
            fptr=nums[nums[fptr]]
            if sptr==fptr:
                break
        
        sptr2=0
        while True:
            sptr=nums[sptr]
            sptr2=nums[sptr2]
            if sptr==sptr2:
                break
        return sptr
            
        