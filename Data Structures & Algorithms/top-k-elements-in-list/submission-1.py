class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        res_list = []
        for n in nums:
            res[n] = 1 + res.get(n, 0)
        
        for num, cnt in res.items():
            res_list.append([cnt, num])
        res_list.sort()
        
        count = []
        while len(count) < k:
            count.append(res_list.pop()[1])
            
        return count