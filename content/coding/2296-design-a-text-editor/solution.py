min2 = lambda a, b: a if a <= b else b


class TextEditor:

    def __init__(self):
        # The cursor is between `self._left` and `self._right`.
        self._left: list[str] = [] # left part of the text
        self._right: list[str] = [] # right part of the text (reversed)

    def addText(self, text: str) -> None:
        self._left.extend(text)

    def deleteText(self, k: int) -> int:
        k = min2(k, len(self._left))
        del self._left[-k:]
        return k

    def cursorLeft(self, k: int) -> str:
        k = min2(k, len(self._left))
        if k > 0:
            self._right.extend(reversed(self._left[-k:]))
            del self._left[-k:]

        return ''.join(self._left[-10:])

    def cursorRight(self, k: int) -> str:
        k = min2(k, len(self._right))
        if k > 0:
            self._left.extend(reversed(self._right[-k:]))
            del self._right[-k:]

        return ''.join(self._left[-10:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
