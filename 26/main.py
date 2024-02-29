from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        search_idx = 1
        correct_idx = 0
        vals = 0
        while search_idx < len(nums):
            if nums[search_idx] != nums[correct_idx]:
                vals += 1
                correct_idx += 1
                search_idx += 1
            else:
                while search_idx < len(nums) and (nums[search_idx] == nums[correct_idx]):
                    search_idx += 1

                if search_idx < len(nums):
                    vals += 1
                    correct_idx += 1
                    nums[correct_idx] = nums[search_idx]

        # import pdb
        # pdb.set_trace()
        # if nums[-1] != nums[correct_idx]:
        #     nums[correct_idx+1] = nums[-1]
        #     vals += 1

        return vals + 1


if __name__ == "__main__":
    s = Solution()

    # my_nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    my_nums = [1, 1, 2]
    print(id(my_nums))
    print(s.removeDuplicates(my_nums))
