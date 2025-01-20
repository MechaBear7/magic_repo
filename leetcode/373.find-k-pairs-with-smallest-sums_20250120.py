"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-20 15:51:32
LastEditors: Helei.Yang
LastEditTime: 2025-01-20 16:07:41
FilePath: /magic_repo/leetcode/373.find-k-pairs-with-smallest-sums_20250120.py
Description: 
"""

#
# @lc app=leetcode.cn id=373 lang=python3
# @lcpr version=30204
#
# [373] 查找和最小的 K 对数字
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from heapq import heappush, heappop
        
        result = []
        my_heap = []
        for j in range(len(nums2)):
            heappush(my_heap, (nums1[0] + nums2[j], 0, j))

        while len(result) < k:
            _, i, j = heappop(my_heap)
            result.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1):
                heappush(my_heap, (nums1[i + 1] + nums2[j], i + 1, j))
        
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

