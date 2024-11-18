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


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        my_heap = []

        for i in range(len(nums1)):
            heappush(my_heap, (nums1[i] + nums2[0], i, 0))

        while k > 0:
            _, i, j = heappop(my_heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heappush(my_heap, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1

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
