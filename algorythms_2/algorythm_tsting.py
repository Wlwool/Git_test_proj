"""

"""


# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#
#     mid = len(nums) // 2
#     left = merge_sort(nums[:mid])
#     right = merge_sort(nums[mid:])
#     print(mid)
#
#     result = []
#
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#
#     return result


# print(insertion_sort([1, 9, 3, 4, 5, 6, 7, 8, 10, 2]))
# print(insertion_sort([5, 3, 4, 1]))
# print(insertion_sort([1, 2, 3, 4]))
# print(merge_sort([10, -1, 3, 7, 2]))
# print(merge_sort([10, 1, 3, 7, 2, 5, 6, 4, 17, 8, 20]))



# def merge(a, b):
#     result = []
#     i = j = 0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             result.append(a[i])
#             i += 1
#         else:
#             result.append(b[j])
#             j += 1
#
#     while i < len(a):
#         result.append(a[i])
#         i += 1
#
#     while j < len(b):
#         result.append(b[j])
#         j += 1
#     return result


# a = [1, 3, 5]
# b = [2, 4, 6]
# print(merge(a, b))
#
# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#
#     mid = len(nums) // 2
#     left = merge_sort(nums[:mid])
#     right = merge_sort(nums[mid:])
#
#     return merge(left, right)


def sliding_window(nums, k):
    result = []
    left = 0
    right = k

    while right <= len(nums):
        result.append(nums[left:right])
        left += 1
        right += 1

    return result



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3

print(sliding_window(nums, k))