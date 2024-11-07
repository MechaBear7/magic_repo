#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30204
#
# [20] 有效的括号
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "]": "[", "}": "{"}
        data = []
        for d in s:
            if d in hashmap:
                if len(data) == 0 or data[-1] != hashmap[d]:
                    return False
                else:
                    data.pop()
            else:
                data.append(d)
        return len(data) == 0


# @lc code=end


#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

#
