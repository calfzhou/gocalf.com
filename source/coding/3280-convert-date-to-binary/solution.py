class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(bin(int(x))[2:] for x in date.split('-'))
