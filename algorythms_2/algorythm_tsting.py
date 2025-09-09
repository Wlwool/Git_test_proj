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

#
# def sliding_window(nums, k):
#     result = []
#     left = 0
#     right = k
#
#     while right <= len(nums):
#         result.append(nums[left:right])
#         left += 1
#         right += 1
#
#     return result
#
#
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = 3
#
# print(sliding_window(nums, k))

# def fib_memo(n, memo={}):
#     if n in memo:
#         print(f"Извлекаем из memo[{n}] = {memo[n]}")
#         return memo[n]
#
#     if n <= 1:
#         print(f"База: fib({n}) = {n}")
#         return n
#
#     print(f"Вычисляем fib({n}) через fib({n-1}) + fib({n-2})")
#     memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
#     print(f"Сохраняем memo[{n}] = {memo[n]}")
#     return memo[n]
#
#
# print("Результат:", fib_memo(5))

# def climb_stairs(n, memo={}):
#     for i in range(len(cost)-3, -1, -1):
#         cost[i] += min(cost[i+1], cost[i+2])
#
#     return min(cost[0], cost[1])
#
#
#
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# print(climb_stairs(10, cost))

# import heapq
# from collections import Counter
#
# def top_k_frequent(nums, k):
#     # counts = Counter(nums)
#     # if k == len(counts):
#     #     return counts.keys()
#     # else:
#     #     return heapq.nlargest(k, counts.keys(), key=counts.get)
#     heap = []
#     for num, freq in Counter(nums).items():
#         if len(heap) > k:
#             heapq.heappush(heap, (freq, num))
#         else:
#             heapq.heappush(heap, (freq, num))
#     return [num for freq, num in heapq.nlargest(k, heap)]
#
#
# nums = [1,1,1,2,2,3,3,3,3]
# k = 2
# print(top_k_frequent(nums, k))  # [3, 1] или [3, 2] (правильно: самые частые)


# import heapq
#
# class PriorityQueue:
#     def __init__(self):
#         self.heap = []
#
#     def enqueue(self, value, priority):
#         heapq.heappush(self.heap, (priority, value))
#
#     def dequeue(self):
#         if not self.is_empty():
#             heapq.heappop(self.heap)
#         return None
#
#     def peek(self):
#         if not self.is_empty():
#             return self.heap[0]
#         else:
#             return None
#
#     def is_empty(self):
#         return len(self.heap) == 0
#
#
# pq = PriorityQueue()
# pq.enqueue("task1", 3)
# pq.enqueue("task2", 1)
# pq.enqueue("task3", 2)
#
# print(pq.dequeue())  # ("task2", 1) — у него самый высокий приоритет
# print(pq.peek())     # ("task3", 2)
#























