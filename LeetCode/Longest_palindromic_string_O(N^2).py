class Solution:
    def longestPalindrome(self, s: str) -> str:
        palin = ''

        #odd len palindrome
        for i in range(len(s)):
            if len(palin) > len(s)//2 + 1 and i > len(s)//2 + 1:
                break
            start = i-1
            end = i+1
            temp_palin = s[i]
            while start >= 0 and end < len(s) and s[start] == s[end]:
                temp_palin = s[start] + temp_palin + s[end]
                start -= 1
                end += 1
            if len(temp_palin) > len(palin):
                palin = temp_palin

        #even len palindrom
        pntr = 0
        while pntr+1 < len(s):
            if len(palin) > len(s)//2 + 1 and pntr > len(s) // 2 + 1:
                break
            if s[pntr] == s[pntr+1]:
                temp_palin = s[pntr]+s[pntr+1]
                start, end = pntr-1, pntr+2
                while start >= 0 and end < len(s) and s[start] == s[end]:
                    temp_palin = s[start]+temp_palin+s[end]
                    start -= 1
                    end += 1
                if len(temp_palin) > len(palin):
                    palin = temp_palin
            pntr += 1

        return(palin)
