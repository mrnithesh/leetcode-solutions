class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashmap = defaultdict(int)
        result = 0
        for i in dominoes:
            hashmap[tuple(sorted(i))] += 1
        for count in hashmap.values():
            result += count * (count-1) // 2
        return result
