class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahren = celsius * 1.80 + 32.00
        answer = [kelvin, fahren]
        return answer
        
