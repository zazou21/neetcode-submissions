class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            heaviest=heapq.heappop_max(stones)
            secondHeaviest=heapq.heappop_max(stones)
            if heaviest == secondHeaviest:
                continue
            if heaviest>secondHeaviest:
                newWeight= heaviest - secondHeaviest
                heapq.heappush_max(stones,newWeight)
        return heapq.heappop_max(stones) if len(stones) > 0 else 0
        