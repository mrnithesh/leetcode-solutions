class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]

        for current in intervals[1:]:
            if current[0] <= prev[1]: #overlapping
                prev[1] = max(prev[1],current[1])
            else:
                res.append(prev)
                prev = current
        res.append(prev)
        return res