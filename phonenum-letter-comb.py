class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numflag = (digits != "") #Checks if digits not empty
        inp = [digits]
        output = []
        endindex = 0
        tempdigit = "2"
        tempstr = ""
        tempindex = 0
        while numflag:
            numflag = False
            inp = inp[endindex:]
            print(inp)
            endindex = len(inp)
            for s in inp:
                if s[-1].isdigit():
                    for i in range(len(s)):
                        if s[i].isdigit():
                            numflag = True
                            tempdigit = s[i]
                            tempindex = i
                            break
                    tempstr = self.chToStr(tempdigit)
                    for tempch in tempstr:
                        inp.append(s[:tempindex] + tempch + s[tempindex+1:])
                else:
                    if s not in output:
                        output.append(s)
        return output

    def chToStr(self, ch):
        if ch == "2":
            return "abc"
        elif ch == "3":
            return "def"
        elif ch == "4":
            return "ghi"
        elif ch == "5":
            return "jkl"
        elif ch == "6":
            return "mno"
        elif ch == "7":
            return "pqrs"
        elif ch == "8":
            return "tuv"
        elif ch == "9":
            return "wxyz"
