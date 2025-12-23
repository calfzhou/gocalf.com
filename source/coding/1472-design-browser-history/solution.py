class BrowserHistory:

    def __init__(self, homepage: str):
        self._history = [homepage]
        self._current = 0
        self._last = self._current

    def visit(self, url: str) -> None:
        self._current += 1
        self._last = self._current
        if self._current == len(self._history):
            self._history.append(url)
        else:
            self._history[self._current] = url

    def back(self, steps: int) -> str:
        self._current -= steps
        if self._current < 0:
            self._current = 0
        return self._history[self._current]

    def forward(self, steps: int) -> str:
        self._current += steps
        if self._current > self._last:
            self._current = self._last
        return self._history[self._current]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
