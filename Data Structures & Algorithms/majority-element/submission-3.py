class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        n = len(nums) / 2

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

            if hash_map[num] > n:
                return num


    # def majorityElement(self, nums: List[int]) -> int:
    #     count = 0
    #     candidate = None

    #     for num in nums:
    #         if count == 0:
    #             candidate = num
    #         count += 1 if candidate == num else -1
    #     return candidate

