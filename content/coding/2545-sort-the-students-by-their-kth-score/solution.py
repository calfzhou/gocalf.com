class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        score.sort(key=lambda row: row[k], reverse=True)
        return score
