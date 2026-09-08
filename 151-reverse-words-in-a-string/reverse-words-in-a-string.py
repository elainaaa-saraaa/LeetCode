class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        l=[]
        for i in range(-1,-len(s)-1,-1):
            l.append(s[i])
        return (' '.join(l))
        