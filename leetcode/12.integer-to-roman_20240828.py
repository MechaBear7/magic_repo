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
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        ans = ""
        for key in hashmap.keys():
            if num >= hashmap[key]:
                count = num // hashmap[key]
                num = num % hashmap[key]
                ans += count * key
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
