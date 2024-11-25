#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30204
#
# [4] 寻找两个正序数组的中位数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = -1, m
        while left + 1 < right:
            i = (left + right) // 2
            j = (m + n - 3) // 2 - i
            if j + 1 == n or nums1[i] <= nums2[j + 1]:
                left = i
            else:
                right = i

        i = left
        j = (m + n - 3) // 2 - i
        a1 = nums1[i] if i >= 0 else -float("inf")
        b1 = nums2[j] if j >= 0 else -float("inf")
        a2 = nums1[i + 1] if i + 1 < m else float("inf")
        b2 = nums2[j + 1] if j + 1 < n else float("inf")

        max_res = max(a1, b1)
        min_res = min(a2, b2)

        return max_res if (m + n) % 2 == 1 else (max_res + min_res) / 2


# @lc code=end


#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#
