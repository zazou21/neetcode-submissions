class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[math.sqrt((points[i][0] - 0)**2 + (points[i][1] - 0)**2) ,i] for i in range(len(points))] 
        heapq.heapify_max(distances)
        while len(distances) > k :
            heapq.heappop_max(distances)
        result = []
        while distances:
            dist , idx = heapq.heappop_max(distances)
            result.append(points[idx])
        return result


