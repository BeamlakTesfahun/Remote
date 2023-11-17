class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
           return False
        divider = 1
        while x >= 10 * divider:
            divider *= 10
        while x:
            right = x % 10 #right digit
            left = x // divider #left digit
            if right != left:
                return False
            #to chop off left and right digits
            x = (x % divider) // 10
            divider /= 100
        return True
