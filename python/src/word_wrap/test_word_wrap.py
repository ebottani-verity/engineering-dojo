import unittest

from src.word_wrap.word_wrap_blausten import WordWrapBlausten
from src.word_wrap.word_wrap_blausten2 import WordWrapBlausten2
from src.word_wrap.word_wrap_kofler_loop import WordWrapKoflerLoop
from src.word_wrap.word_wrap_kofler_regex import WordWrapKoflerRegex
from src.word_wrap.word_wrap_martin import WordWrapMartin


# Assuming the translated classes are imported correctly
# from word_wrap_blausten import WordWrapBlausten
# from word_wrap_blausten2 import WordWrapBlausten2
# from word_wrap_kofler_loop import WordWrapKoflerLoop
# from word_wrap_kofler_regex import WordWrapKoflerRegex
# from word_wrap_martin import WordWrapMartin

class TestWordWrap(unittest.TestCase):

    def test_wraps_empty_string(self):
        implementations = [
            ("WordWrapBlausten", WordWrapBlausten()),
            ("WordWrapBlausten2", WordWrapBlausten2()),
            ("WordWrapKoflerLoop", WordWrapKoflerLoop()),
            ("WordWrapKoflerRegex", WordWrapKoflerRegex()),
            ("WordWrapMartin", WordWrapMartin()),
        ]

        for name, wrapper in implementations:
            with self.subTest(name=name):
                self.assertEqual(wrapper.wrap("", 1), "")

    # TODO: write more test cases using the same pattern

if __name__ == '__main__':
    unittest.main()
