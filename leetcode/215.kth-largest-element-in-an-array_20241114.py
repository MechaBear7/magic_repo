#
# @lc app=leetcode.cn id=215 lang=python3
# @lcpr version=30204
#
# [215] 数组中的第K个最大元素
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(piece_nums, k):
            pivot = random.choice(piece_nums)
            print(pivot, piece_nums)
            small, equal, big = [], [], []

            for i in range(len(piece_nums)):
                if piece_nums[i] == pivot:
                    equal.append(piece_nums[i])
                elif piece_nums[i] < pivot:
                    small.append(piece_nums[i])
                else:
                    big.append(piece_nums[i])

            if k <= len(big):
                return quick_select(big, k)
            elif k > len(equal) + len(big):
                return quick_select(small, k - len(equal) - len(big))
            else:
                return pivot

        return quick_select(nums, k)


# @lc code=end


#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#
