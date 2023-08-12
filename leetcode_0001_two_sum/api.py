"""API for solving problem Two Sum"""

LEN_MAX = 10**4
LEN_MIN = 2

NUM_MAX = 10**9
NUM_MIN = -NUM_MAX

TARGET_MAX = NUM_MAX
TARGET_MIN = NUM_MIN


def _check_preconditions(nums: list[int], target: int) -> bool:
    if not LEN_MIN <= len(nums) <= LEN_MAX:
        return False

    for x in nums:
        if not NUM_MIN <= x <= NUM_MAX:
            return False

    if not TARGET_MIN <= target <= TARGET_MAX:
        return False

    return True


def _sum_difference(x: int, y: int, target: int) -> int:
    pass


def two_sum(nums: list[int], target: int) -> list[int]:
    """Solves problem Two Sum"""

    assert _check_preconditions(nums, target)

    nums = enumerate(nums)
    nums = sorted(nums, key=lambda pair: pair[1])

    it = iter(nums)
    rit = reversed(nums)

    i, x = next(it)
    ri, rx = next(rit)

    while True:
        if (diff := _sum_difference(x, rx, target)) > 0:
            i, x = next(it)
        elif diff < 0:
            ri, rx = next(rit)
        else:
            return [i, ri]
