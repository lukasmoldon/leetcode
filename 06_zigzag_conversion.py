class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = [[] for _ in range(numRows)]

        cur_row = 0
        cur_col = 0

        for char in s:
            
            if cur_col % (numRows-1) == 0:
                result[cur_row].append(char)
                cur_row += 1
                if cur_row == numRows:
                    cur_row = 0
                    cur_col += 1
            else:
                offset = cur_col % (numRows-1)
                for i in range(numRows-offset-1):
                    result[cur_row].append(" ")
                    cur_row += 1
                result[cur_row].append(char)
                cur_row += 1
                for i in range(offset):
                    result[cur_row].append(" ")
                    cur_row += 1
                cur_row = 0
                cur_col += 1

        string_result = ""
        for line in result:
            for char in line:
                if char != " ":
                    string_result += char

        return string_result

if __name__ == '__main__':
    sol_object = Solution()
    output = sol_object.convert("PAYPALISHIRING", 4)
    print(output)