class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x=str(x)
        return (str_x[::-1]==str(x))

    #without converting the integer to a string    
    def isPalindrome(self, x: int) -> bool:
        og=x
        rev=0
        while x>0:
            rev=rev*10 + x%10
            x//=10
        return og==rev