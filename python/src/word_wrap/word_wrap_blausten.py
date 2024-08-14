class WordWrapBlausten:

    def wrap(self, text: str, column_length: int) -> str:
        text_length = len(text)
        if text_length < column_length:
            return text
        chars_array = list(text)
        text_sections = []
        section_count = text_length / column_length
        char_index = 0

        for _ in range(int(section_count)):
            section = ""
            length_till_last_space = char_index + column_length
            print("1st length", length_till_last_space)
            while chars_array[length_till_last_space] != ' ':
                if length_till_last_space >= len(chars_array):
                    raise IndexError(f"ArrayIndexOutOfBoundsException : Index {length_till_last_space} "
                                     f"out of bounds for length {len(chars_array)}")
                length_till_last_space -= 1

            chars_in_this_section = length_till_last_space - char_index
            print("2nd length", length_till_last_space)
            for _ in range(chars_in_this_section):
                section += chars_array[char_index]
                char_index += 1
            print("Index", char_index)
            text_sections.append(section.strip())

        print("Near index", char_index)
        print("Text Length", text_length)
        remaining_chars = text_length % char_index
        print("Remaining", remaining_chars)
        if remaining_chars > 0:
            section = ""
            for _ in range(remaining_chars):
                section += chars_array[char_index]
                char_index += 1
            print("Final index", char_index)
            print("TotalChars", len(chars_array))
            text_sections.append(section.strip())

        print(text_sections[1] if len(text_sections) > 1 else "No second section")
        return "\n".join(text_sections)
