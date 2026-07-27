class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l=0
        r=len(height)-1
        trapped=0
        l_max=height[0]
        r_max=height[r]
        while l<r:
            if l_max<r_max:
                l+=1
                l_max=max(height[l],l_max)
                water=l_max-height[l]
                water=max(0,water)
                trapped+=water
            else:
                r-=1
                r_max=max(height[r],r_max)
                water=r_max-height[r]
                water=max(0,water)
                trapped+=water
        return trapped



        



        