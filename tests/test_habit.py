from app.domain.habit import Habit
from datetime import date
import pytest

def test_create_valid_habit():
    habit = Habit(
        id="h01",
        name="Drink Water",
        description="Drink 8 glasses daily",
        frequency="daily",
        start_date=date.today()
    )

    assert habit.name == "Drink Water"

def test_invalid_frequency():
    with pytest.raises(ValueError):
        Habit(
            id="h02",
            name="Test",
            description=None,
            frequency="yearly",
            start_date=date.today()
        )