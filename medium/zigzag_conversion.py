class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        og_index = 2*(numRows-1)
        next_index = og_index
        index = 0
        column_pass = 0
        output = ""
        for i in range(numRows):
            if i == numRows-1: next_index = og_index
            index = 0
            column_pass = 0

            while index < len(s):
                output += s[index]
                if index % og_index != 0: 
                    column_pass += og_index
                    index = column_pass
                else: index += next_index

            s = s[1:]
            next_index -= 2

        return output
    
assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"