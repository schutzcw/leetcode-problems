from typing import List

# Note: my original solution had another count variable that was wasting cycles. correct_idx
# maintains the count already in the index


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        correct_idx = 0
        for _, value in enumerate(nums):
            if value == val:
                continue
            nums[correct_idx] = value
            correct_idx += 1
        return correct_idx


if __name__ == "__main__":

    nums = [3, 2, 2, 3]
    val = 3

    s = Solution()
    k = s.removeElement(nums, val)

    print(nums)
    print(k)
