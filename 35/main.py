from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        low_idx = 0
        high_idx = len(nums) - 1
        while high_idx > low_idx:
            mid_idx = low_idx + ((high_idx - low_idx) // 2)
            print(f"li: {low_idx}, hi: {high_idx}, mi: {mid_idx}")
            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] > target:
                high_idx = mid_idx - 1
            else:
                low_idx = mid_idx + 1

        import pdb
        pdb.set_trace()
        if target > nums[low_idx]:
            return low_idx + 1
        else:
            return low_idx


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 5, 6]
    # print(f"Result: {s.searchInsert(nums, 5)}")
    print(f"Result: {s.searchInsert(nums, 2)}")
    # print(f"Result: {s.searchInsert(nums, 7)}")
    # print(f"Result: {s.searchInsert(nums, 0)}")

    # nums = [1, 3]
    # print(f"Result: {s.searchInsert(nums, 0)}")
