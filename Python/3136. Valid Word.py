class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vowels = ['a','e','i','o','u']
        cons = False
        vow = False
        for i in word:
            if not i.isalnum():
                return False
            elif i.isalpha():
                if i.lower() in vowels:
                    vow = True
                elif i.lower() not in vowels:
                    cons = True
        return cons and vow