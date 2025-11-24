from dataclasses import dataclass, asdict

@dataclass
class User:
    id: int
    name: str
    student_id: str  # a unique identifier such as roll number

    def to_dict(self):
        return asdict(self)
