class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_map = {}

        for str_ in strs:
            list_map = [0] * (ord("z") - ord("a") + 1)

            for ch in str_:
                s = ord(ch) - ord("a")
                list_map[s] += 1
            
            dict_map.setdefault(tuple(list_map), []).append(str_)

        return [d for d in dict_map.values()]