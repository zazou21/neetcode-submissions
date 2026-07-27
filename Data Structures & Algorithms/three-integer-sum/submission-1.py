class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        print("hello")
        result=[]
        nums.sort()
        ptr=0
        while ptr<len(nums)-1:
            if ptr>0 and nums[ptr]==nums[ptr-1]:
                ptr+=1
                continue
            l=ptr+1
            r=len(nums)-1
            target=-nums[ptr]
            
            while l<r:
                if nums[l] + nums[r]==target:
                    result.append([nums[ptr],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
                elif nums[l]+nums[r]<target:
                    l+=1
            ptr+=1
        return result

       

    


         
            
                
            
