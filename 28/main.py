from typing import List

# Note: my original solution had another count variable that was wasting cycles. correct_idx
# maintains the count already in the index


# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         idx = 0
#         MAX_START_IDX = len(haystack) - len(needle)
#         while (MAX_START_IDX - idx) >= 0:
#             for j, needle_char in enumerate(needle):
#                 if haystack[i+j] != needle_char:
#                     break
#                 if j == len(needle) - 1:
#                     return i
#         return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = 0
        MAX_START_IDX = len(haystack) - len(needle)
        while (MAX_START_IDX - idx) >= 0:
            for j, needle_char in enumerate(needle):
                print(
                    f"idx: {idx}, haystack[{idx+j}]: {haystack[idx+j]}, needle_char: {needle_char}")
                if haystack[idx+j] != needle_char:
                    print("break")
                    idx = idx+j+1
                    break
                if j == len(needle) - 1:
                    return idx
            print(
                f"MAX_START_IDX: {MAX_START_IDX}, idx: {idx}, MAX_START_IDX - idx: {MAX_START_IDX - idx}")
        return -1

    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        print(f"low: {low}, high: {high}")
        while (high - low) > 1:
            idx = (high - low) // 2
            print(idx)
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                high = idx
            else:
                low = idx
            print(f"low: {low}, high: {high}")
        return high


if __name__ == "__main__":

    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 7))
    # val = s.strStr("mississippi", "issip")

    # print(val)
