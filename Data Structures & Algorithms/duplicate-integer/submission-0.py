class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_map = set()

        for num in nums:
            if num in set_map:
                return True
                
            set_map.add(num)

        return False