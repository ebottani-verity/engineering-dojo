BLANK = ' '
NEWLINE = '\n'


class WordWrapKoflerLoop:

    def wrap(self, line: str, max_line_len: int) -> str:
        accumulator = StringBuilder()
        remaining_line = line
        while len(remaining_line) > max_line_len:
            index_of_blank = remaining_line.rfind(BLANK, 0, max_line_len)
            if index_of_blank > -1:
                split = index_of_blank
                offset = 1
            else:
                split = max_line_len
                offset = 0

            accumulator.append(remaining_line[:split])
            accumulator.append(NEWLINE)
            remaining_line = remaining_line[split + offset:]

        accumulator.append(remaining_line)
        return accumulator.to_string()


class StringBuilder:

    def __init__(self):
        self.str_array = []

    def get(self, n_index: int) -> str:
        if 0 <= n_index < len(self.str_array):
            return self.str_array[n_index]
        return None

    def is_empty(self) -> bool:
        return len(self.str_array) == 0

    def append(self, s: str):
        if s is not None:
            self.str_array.append(s)

    def to_string(self) -> str:
        return "".join(self.str_array)

    def to_array_string(self, delimiter: str) -> str:
        return delimiter.join(self.str_array)

    def clear(self):
        self.str_array.clear()
