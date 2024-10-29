#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30204
#
# [322] 零钱兑换
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        # 初始化 dp 数组
        dp = [float("inf") for _ in range(amount + 1)]
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(amount + 1):
            min_coin = dp[i]
            for coin in coins:
                if i - coin >= 0:
                    min_coin = min(min_coin, dp[i - coin] + 1)
            dp[i] = min_coin

        return -1 if dp[amount] == float("inf") else dp[amount]


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

#
