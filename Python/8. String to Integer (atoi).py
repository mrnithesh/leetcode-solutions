class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        res=[]
        i=0
        sign=1
        if not s:
            return 0
        if s[0]=="-":
            sign=-1
            i+=1
        elif s[0]=="+":
            sign=+1
            i+=1
        #print(s)
        while i <len(s) and s[i].isdigit():
            #print(s[i])
            res.append(s[i])
            i+=1
        #print(res)
        if not res:
            return 0
    
        integer=int("".join(res))*sign
        
        int_max=2**31-1
        int_min=-2**31
        if integer>int_max:
            return int_max
        elif integer<int_min:
            return int_min
        
        return integer