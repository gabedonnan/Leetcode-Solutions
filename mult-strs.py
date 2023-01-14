class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total = 0
        for i,digit in enumerate(num1[::-1]):
            for j, digit2 in enumerate(num2[::-1]):
                total += (self.chtoi(digit) * (10 ** i)) * (self.chtoi(digit2) * (10 ** j))
        return str(total)     

    def chtoi(self, ch: str) -> int:
        if ch == "0":
            return 0
        elif ch == "1":
            return 1
        elif ch == "2":
            return 2
        elif ch == "3":
            return 3
        elif ch == "4":
            return 4
        elif ch == "5":
            return 5
        elif ch == "6":
            return 6
        elif ch == "7":
            return 7
        elif ch == "8":
            return 8
        elif ch == "9":
            return 9
        else:
            raise Error("bronkened")
