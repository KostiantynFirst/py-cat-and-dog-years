from app.main import get_human_age


def test_zero_ages_returns_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_ages_below_15_returns_zeros() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_15_years_returns_one() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_16_to_23_years_returns_one() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_24_years_returns_two() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_25_to_27_years_returns_two() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_28_years_returns_three_dog_returns_two() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
