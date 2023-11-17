class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        i = 0
        counter = 0
        while i < len(hours):
            if hours[i] >= target:
                counter += 1
            i += 1
        return counter
        
