class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        hash_set = set()
        _max = 0

        for fast in range(len(s)):
            while s[fast] in hash_set:
                hash_set.remove(s[slow])
                slow += 1

            hash_set.add(s[fast])

            if (fast - slow + 1) > _max:
                _max = fast  - slow + 1 

        return _max