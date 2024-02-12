import pytest
from src.utils import normalize_date

# Test cases for the normalize_date function
@pytest.mark.parametrize("test_input,expected", [
    ("01/01/2020", "2020-01-01"),
    ("02/01/2020", "2020-01-02"),
    ("2020-01-01", "2020-01-01"),
    ("1 January 2020", "2020-01-01"),
    ("25/05/2020", "2020-05-25"),
])
def test_normalize_date(test_input, expected):
    assert normalize_date(test_input) == expected, f"Failed for {test_input}"
