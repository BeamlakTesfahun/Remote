class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = 0
        y = len(nums)//2
        answer = []
        while x < len(nums)//2:
            answer.append(nums[x])
            answer.append(nums[y])
            x = x + 1
            y = y + 1 
        return answer

        
