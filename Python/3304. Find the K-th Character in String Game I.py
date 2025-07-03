class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while True:
            if len(word)>k:
                return word[k-1]
            else:
                genStr = ''
                for ch in word:
                    if ch == 'z':
                        word+='a'
                    else:
                        genStr += chr(ord(ch)+1)
                word+=genStr
                print(word)
            