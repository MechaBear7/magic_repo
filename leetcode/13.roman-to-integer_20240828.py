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
        hashmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        n = len(s)
        for i in range(n - 1):
            if hashmap[s[i]] < hashmap[s[i + 1]]:
                ans -= hashmap[s[i]]
            else:
                ans += hashmap[s[i]]
        ans += hashmap[s[-1]]
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
