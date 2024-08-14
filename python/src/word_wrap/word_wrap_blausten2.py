class WordWrapBlausten2:
    def wrap(self, line: str, max_line_len: int) -> str:
        return wrap_static(line, max_line_len)


def wrap_static(text: str, cols: int) -> str:
    if cols >= len(text):
        return text
    cols_to_space = text.rfind(' ', 0, cols)
    actual_cols = cols_to_space + 1 if cols_to_space != -1 else cols
    if text[cols] == ' ':
        actual_cols = cols + 1
    return text[:actual_cols] + "\n" + wrap_static(text[actual_cols:], cols)
