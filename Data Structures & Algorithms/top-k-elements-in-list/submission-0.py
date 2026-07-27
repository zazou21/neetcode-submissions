class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for num in nums:
            if num not in hashmap:
                hashmap[num]=1
            else:
                hashmap[num]+=1
        output=dict(sorted(hashmap.items(), key=lambda item: item[1],reverse=True))
        print(output)
        return list(output.keys())[:k]
        
        