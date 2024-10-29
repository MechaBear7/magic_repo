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
        ans = 0
        map_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        for i in range(0, n - 1):
            if map_dict[s[i]] < map_dict[s[i + 1]]:
                ans -= map_dict[s[i]]
            else:
                ans += map_dict[s[i]]
        ans += map_dict[s[-1]]
        return ans


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
