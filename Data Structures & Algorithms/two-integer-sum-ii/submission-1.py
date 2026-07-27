class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #rp moves the number decreases
        #lp moves the number increases
        l=0
        r=len(numbers)-1
        while l<r:
            if numbers[r]+numbers[l]==target:
                return [l+1,r+1]
            if numbers[r]>target and numbers[l]>0:
                r-=1
                continue
            if numbers[r]<target and numbers[l]<0:
                l+=1
                continue
            if numbers[r]+numbers[l]>target:
                r-=1
            else:
                l+=1
        return[]

            
            
           







        