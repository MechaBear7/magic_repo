#
# @lc app=leetcode.cn id=LCR 103 lang=python3
# @lcpr version=30204
#
# [LCR 103] 零钱兑换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] 代表构成 i 元需要的最少硬币数
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0  # 0 元需要 0 个硬币

        for i in range(amount + 1):
            if dp[i] != float("inf"):
                for coin in coins:
                    if i + coin <= amount:
                        dp[i + coin] = min(dp[i + coin], dp[i] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1




# @lc code=end



#
# @lcpr case=start
# [1, 2, 5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1]\n2\n
# @lcpr case=end

#

