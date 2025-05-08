class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hashmap = defaultdict(int)
        paragraph = re.sub(r"[^\w\s]"," ",paragraph)
        paragraph = paragraph.split()
        for i in paragraph:
            if i.lower() not in banned:
                hashmap[i.lower()] += 1
        result = max(hashmap,key=hashmap.get)
        return result