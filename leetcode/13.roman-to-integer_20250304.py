#
# @lc app=leetcode.cn id=13 lang=python3
# @lcpr version=30204
#
# [13] 罗马数字转整数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        result = 0
        for i in range(len(s) - 1):
            if hashmap[s[i]] < hashmap[s[i+1]]:
                result -= hashmap[s[i]]
            else:
                result += hashmap[s[i]]
        result += hashmap[s[-1]]
        return result

# @lc code=end



#
# @lcpr case=start
# "III"\n
# @lcpr case=end

# @lcpr case=start
# "IV"\n
# @lcpr case=end

# @lcpr case=start
# "IX"\n
# @lcpr case=end

# @lcpr case=start
# "LVIII"\n
# @lcpr case=end

# @lcpr case=start
# "MCMXCIV"\n
# @lcpr case=end

#

