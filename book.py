from dataclasses import dataclass, asdict

@dataclass
class Book:
    id: int
    title: str
    author: str
    isbn: str
    copies: int

    def to_dict(self):
        return asdict(self)
