class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = {}
        for n in nums:
            if n not in count_map:
                count_map[n] = 1
            else:
                return True
        return False