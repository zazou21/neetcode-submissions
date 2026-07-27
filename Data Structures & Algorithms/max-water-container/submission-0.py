class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maximum_water=0
        while l<r:
            height=min(heights[l],heights[r])
            width=r-l
            area=height*width
            maximum_water=max(area,maximum_water)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return maximum_water


        