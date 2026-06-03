from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []

        for words in strs:
            sorted_words = tuple(sorted(words))
            anagram_map[sorted_words].append(words)

        for val in anagram_map.values():
            result.append(val)

        return result