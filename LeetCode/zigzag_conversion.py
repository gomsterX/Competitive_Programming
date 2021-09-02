class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = [""] * numRows
        reverse = False
        loop = -1
        if numRows == 1:
            return s
        else:
            for i in range(len(s)):
                if reverse:
                    if loop == 1:
                        reverse = False
                    loop -= 1
                else:
                    loop += 1
                    if loop == numRows - 1:
                        reverse = True
                l[loop] += s[i]


            return(''.join(l))


        
