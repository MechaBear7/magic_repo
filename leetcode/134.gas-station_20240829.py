#
# @lc app=leetcode.cn id=134 lang=python3
# @lcpr version=30204
#
# [134] 加油站
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        当遍历全部加油站一次的gas总量减去cost总量大于0则满足按顺序绕环路行驶一周的要求，否则不满足。
        途中最小值很可能是一个负值，这个负值的绝对值最大代表油量亏欠到了最大值，
        则从0号加油站到现在会亏欠最多的油量，那么从下一个加油站开始行使到最后一个加油站会永远保持正值的油量，
        再行驶至上一个加油站也仍然为正值。
        """
        n = len(gas)
        cur_gas = 0
        min_idx = 0
        min_gas = float("inf")
        for i in range(n):
            cur_gas += gas[i] - cost[i]
            if cur_gas < min_gas:
                min_idx = i
                min_gas = cur_gas
        return -1 if cur_gas < 0 else (min_idx + 1) % n


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n[3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n[3,4,3]\n
# @lcpr case=end

#
