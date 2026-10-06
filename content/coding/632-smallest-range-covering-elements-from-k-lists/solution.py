class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        k = len(nums)
        leaf = k >> 1
        heap = [(arr[0], arr, 0) for arr in nums] # min heap

        def shift_down(pos: int):
            while pos < leaf:
                left = (pos << 1) + 1
                right = left + 1
                child = right if right < k and heap[right][0] < heap[left][0] else left
                if heap[pos][0] > heap[child][0]:
                    heap[pos], heap[child] = heap[child], heap[pos]
                    pos = child
                else:
                    return

        # Build the heap.
        for i in range(leaf - 1, -1, -1):
            shift_down(i)

        min_l = heap[0][0]
        r = max(arr[0] for arr in nums)
        min_len = r - min_l
        while (j := heap[0][2]) < len(heap[0][1]) - 1:
            heap[0] = (heap[0][1][j+1], heap[0][1], j+1)
            r = max(r, heap[0][0])
            shift_down(0)
            if (cur_len := r - heap[0][0]) < min_len:
                min_len = cur_len
                min_l = heap[0][0]

        return [min_l, min_l + min_len]
