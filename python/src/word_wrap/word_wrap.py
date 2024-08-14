from abc import ABC, abstractmethod

class WordWrap(ABC):
    @abstractmethod
    def wrap(self, line: str, max_line_len: int) -> str:
        pass
