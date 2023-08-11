"""Tests API for solving problem Two Sum"""

import pytest

from leetcode_0001_two_sum import api


@pytest.mark.parametrize(
    ["result", "nums", "target"],
    (
        [..., ...],
        [..., ...],
    ),
)
def test_two_sum(result, nums: list[int], target: int) -> None:
    """Tests solution for problem Two Sum"""

    assert api.two_sum(nums, target) == result
