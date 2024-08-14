import re

NEWLINE = '\n'

class WordWrapKoflerRegex:

    def wrap(self, line: str, max_line_len: int) -> str:
        pattern = (
            "([^ ]{" + str(max_line_len) + "})"  # force split after exact max_line_len of non-spaces
            "(?=[^ ])"  # which must be followed by a non-space
            "|"  # or
            "(?=.{" + str(max_line_len) + "}.)"  # if we have more than max_line_len characters here, then
            "(.{1," + str(max_line_len) + "})"  # wrap at most after max_line_len characters
            " "  # and drop the space afterward
        )
        return re.sub(pattern, r"\1\2" + NEWLINE, line)
