#
# @lc app=leetcode.cn id=373 lang=python3
# @lcpr version=30204
#
# [373] 查找和最小的 K 对数字
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
from heapq import heappush, heappop
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        m, n = len(nums1), len(nums2)
        result = []
        min_heap = []

        # Initialize the heap with pairs (nums1[i], nums2[0]) for i from 0 to min(m, k) - 1
        for i in range(min(m, k)):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        # Extract the k smallest pairs from the heap
        while k > 0 and min_heap:
            total, i, j = heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1

            # If there's another element in nums2 for nums1[i], push the next pair
            if j + 1 < n:
                heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result


# @lc code=end


#
# @lcpr case=start
# [1,7,11]\n[2,4,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n[1,2,3]\n2\n
# @lcpr case=end

#
