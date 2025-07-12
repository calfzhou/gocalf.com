class ATM:

    def __init__(self):
        self._notes = [20, 50, 100, 200, 500]
        self._counts = [0] * 5

    def deposit(self, banknotesCount: list[int]) -> None:
        for i, cnt in enumerate(banknotesCount):
            self._counts[i] += cnt

    def withdraw(self, amount: int) -> list[int]:
        used = [0] * 5
        for i in range(4, -1, -1):
            note = self._notes[i]
            if self._counts[i] > 0 and (cnt := amount // note) > 0:
                cnt = min(cnt, self._counts[i])
                used[i] = cnt
                amount -= note * cnt
                if amount == 0: break
        else:
            return [-1]

        for i, cnt in enumerate(used):
            self._counts[i] -= cnt
        return used


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
