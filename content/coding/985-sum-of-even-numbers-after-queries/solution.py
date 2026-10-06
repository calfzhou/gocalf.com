class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        even_sum = sum(x for x in nums if x & 1 == 0)
        m = len(queries)
        answer = [0] * m
        for i, (diff, j) in enumerate(queries):
            orig = nums[j]
            nums[j] += diff
            if orig & 1:
                if diff & 1:
                    even_sum += nums[j] # odd => even: add the updated number to the sum.
            else:
                if diff & 1:
                    even_sum -= orig # even => odd: sub the original number from the sum.
                else:
                    even_sum += diff # even => even: add the diff to the sum.

            answer[i] = even_sum

        return answer
