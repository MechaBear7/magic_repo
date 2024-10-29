#
# @lc app=leetcode.cn id=12 lang=python3
# @lcpr version=30204
#
# [12] 整数转罗马数字
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        result = ""
        for key, value in hashmap.items():
            if num >= key:
                result += (num // key) * value
                num = num % key
        return result


# @lc code=end


#
# @lcpr case=start
# 3749\n
# @lcpr case=end

# @lcpr case=start
# 58\n
# @lcpr case=end

# @lcpr case=start
# 1994\n
# @lcpr case=end

#
