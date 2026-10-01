class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        ogcount= len(nums)
        while len(nums) > ogcount - k + 1:
            heapq.heappop_max(nums)
        return heapq.heappop_max(nums)

        