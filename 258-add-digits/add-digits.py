class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10: 
            x= 0
            while num > 0:
                x+=num % 10  
                num//=10         
            num=x
        return num
'''
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
'''