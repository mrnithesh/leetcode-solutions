class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            res= defaultdict(list)
            for i in strs :
                count=[0] * 26 #hashmap 
                for c in i :
                    count[ord(c)-ord('a')]+=1 #key using ascii values 
                res[tuple(count)].append(i)
            return list(res.values())
                                                                                        