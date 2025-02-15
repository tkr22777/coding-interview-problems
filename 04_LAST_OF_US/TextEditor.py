class TextEditor:
    def __init__(self):
        self.left = ""
        self.right = ""

    def print(self):
        print(f"left:'{self.left}' , right:'{self.right}'")

    def addText(self, text: str) -> None:
        self.left += text
        # self.print()

    def deleteText(self, k: int) -> int:
        cur_size = len(self.left)
        max_delete = min(cur_size, k)
        self.left = self.left[:cur_size - max_delete]
        # self.print()
        return max_delete

    def cursorLeft(self, k: int) -> str:
        i = len(self.left) - min(len(self.left), k)
        self.right = self.left[i:] + self.right
        self.left = self.left[:i]
        # self.print()
        i = len(self.left) - min(10, len(self.left))
        return self.left[i:]

    def cursorRight(self, k: int) -> str:
        self.left = self.left + self.right[:k]
        self.right = self.right[k:]
        i = len(self.left) - min(10, len(self.left))
        # self.print()
        return self.left[i:]


# Better two stack/list solution

class TextEditor2:

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
t.print()
t.deleteText(1)
t.print()
t.deleteText(11)
t.print()
t.addText("mns")
t.print()
t.deleteText(1)
t.print()
t.addText("asdfas")
t.print()
t.cursorLeft(1)
t.print()
t.cursorLeft(5)
t.print()
t.cursorLeft(5)
t.print()
t.cursorLeft(5)
t.print()
t.cursorRight(1)
t.print()
t.cursorRight(1)
t.print()
t.cursorRight(3)
t.print() 