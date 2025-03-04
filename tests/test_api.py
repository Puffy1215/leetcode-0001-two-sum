"""Tests API for solving problem Two Sum"""

import pytest

from leetcode_0001_two_sum import api


@pytest.mark.parametrize(
    ["result", "nums", "target"],
    (
        [[0, 1], [2, 7, 11, 15], 9],
        [[1, 2], [3, 2, 4], 6],
        [[0, 1], [3, 3], 6],
    ),
)
def test_two_sum(result: list[int], nums: list[int], target: int) -> None:
    """Tests solution for problem Two Sum"""

    assert api.two_sum(nums, target) == result
