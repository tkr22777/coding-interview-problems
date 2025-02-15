class TextEditor:
    def __init__(self):
        # Two stacks that are relative to the cursor, r is in reverse
        self.l, self.r = [], []

    def addText(self, text: str) -> None:
        self.l.extend(list(text))

    def deleteText(self, k: int) -> int:
        length = min(k, len(self.l))
        for _ in range(length):
            self.l.pop()
        return length

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.l))):
            self.r.append(self.l.pop())
        return ''.join(self.l[-10:])

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.r))):
            self.l.append(self.r.pop())
        return ''.join(self.l[-10:])

# Test cases
t = TextEditor()
t.addText("abc")
t.addText("ced")
t.deleteText(1)
t.deleteText(11)
t.addText("mns")
t.deleteText(1)
t.addText("asdfas")
t.cursorLeft(1)
t.cursorLeft(5)
t.cursorLeft(5)
t.cursorLeft(5)
t.cursorRight(1)
t.cursorRight(1)
t.cursorRight(3) 