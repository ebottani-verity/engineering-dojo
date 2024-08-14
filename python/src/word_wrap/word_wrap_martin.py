class WordWrapMartin:

    def wrap(self, line: str, max_line_len: int) -> str:
        return Wrapper.wrap(line, max_line_len)


class Wrapper:

    def __init__(self, col: int):
        self.col = col

    @staticmethod
    def wrap(s: str, col: int) -> str:
        return Wrapper(col).wrap_instance(s)

    def wrap_instance(self, s: str) -> str:
        if len(s) <= self.col:
            return s
        space = s[:self.col].rfind(' ')
        if space != -1:
            return self.break_line(s, space, 1)
        elif s[self.col] == ' ':
            return self.break_line(s, self.col, 1)
        else:
            return self.break_line(s, self.col, 0)

    def break_line(self, s: str, pos: int, gap: int) -> str:
        return s[:pos] + "\n" + Wrapper.wrap(s[pos + gap:], self.col)
