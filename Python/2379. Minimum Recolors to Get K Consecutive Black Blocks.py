class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
            i=0
            j=k
            l=[]
            while j<=len(blocks):
                newstr=blocks[i:j]
                hashmap={"W":0,"B":0}
                #print(newstr)
                for k in newstr:
                    hashmap[k]+=1
                l.append(hashmap.get("W"))
                i+=1
                j+=1
            #print (l)
            return min(l)
