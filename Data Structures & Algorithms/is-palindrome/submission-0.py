class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        
        while i<j:
            if not self.alphaNum(s[i]):
                if i+1>j:
                    return True
                i+=1
                continue
            if not self.alphaNum(s[j]):
                if j-1<i:
                    return True
                j-=1
                continue
            if s[i].lower()!=s[j].lower():
                print(s[i])
                print(s[j])
                return False
            i+=1
            j-=1
        return True

            
                




    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

        