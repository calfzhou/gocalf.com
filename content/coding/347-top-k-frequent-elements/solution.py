class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counting: dict[int, int] = {} # counting[i]: freq of number i.
        for v in nums:
            counting[v] = counting.get(v, 0) + 1

        min_heap = [None] * k
        leaf = k >> 1

        def shift_down(pos: int):
            while pos < leaf:
                left = (pos << 1) + 1
                right = left + 1
                child = right if right < k and min_heap[right][1] < min_heap[left][1] else left
                if min_heap[pos][1] > min_heap[child][1]:
                    min_heap[pos], min_heap[child] = min_heap[child], min_heap[pos]
                    pos = child
                else:
                    return

        for i, item in enumerate(counting.items()):
            if i < k:
                min_heap[i] = item
                if i == k - 1:
                    # Build heap.
                    for j in range(leaf - 1, -1, -1):
                        shift_down(j)
            elif item[1] > min_heap[0][1]:
                # Replace heap top with v.
                min_heap[0] = item
                shift_down(0)

        return [v for v, _ in min_heap]

