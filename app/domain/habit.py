from dataClasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Habit:
    id: str
    name: str
    description: str | None
    frequency: str
    start_date: date