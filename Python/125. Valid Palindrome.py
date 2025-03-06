class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str="".join([i for i in s if i.isalnum()])
        cleaned_str=cleaned_str.lower()
        #two pointers
        left=0
        right=len(cleaned_str)-1
        while left<right:
            if cleaned_str[left]!=cleaned_str[right]:
                return False
            left+=1
            right-=1
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool: #NO TWO POINTERS
        result=""
        for i in s:
            if i.isalnum():
                result+=i
        result=result.lower()
        return result==result[::-1]
              