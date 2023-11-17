class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        numbers = []
        i = 1
        while i<n+1:
            if i%3 == 0 and i%5== 0:
                numbers.append("FizzBuzz")
            elif i%3 == 0:
                numbers.append("Fizz")
            elif i%5 == 0:
                numbers.append("Buzz")
            else:
                numbers.append(str(i))
            i = i + 1
        return numbers
