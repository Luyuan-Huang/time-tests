from times import compute_overlap_time, time_range

import pytest
from times import time_range

def test_time_range_backwards():
    with pytest.raises(ValueError, match="must be after start_time"):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")


def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)

    expected = result
    assert result == expected
