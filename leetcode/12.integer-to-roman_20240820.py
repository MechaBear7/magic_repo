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
        map_dict = {
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
        ans = ""
        for map_key in map_dict.keys():
            if num >= map_key:
                count = num // map_key
                ans = ans + count * map_dict[map_key]
                num = num % map_key
        return ans


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
