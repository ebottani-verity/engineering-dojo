from .leap_year import is_leap_year

# Acceptance criteria
# 1. All years divisible by 400 ARE leap years (so, for example, 2000 was indeed a leap year),

# 2. All years divisible by 100 but not by 400 are NOT leap years (so, for example, 1700, 1800, and 1900 were NOT leap years, NOR will 2100 be a leap year),

# 3. All years divisible by 4 but not by 100 ARE leap years (e.g., 2008, 2012, 2016),

# 4. All years not divisible by 4 are NOT leap years (e.g. 2017, 2018, 2019).


def test_is_divisible_by_400():
    assert is_leap_year(400) == True


def test_is_divisible_by_100_but_not_400():
    for year in (1700, 1800, 1900, 2100):
        assert is_leap_year(year) == False


def test_is_divisible_by_4_but_not_100():
    for year in (2008, 2012, 2016, 404):
        assert is_leap_year(year) == True


def test_is_not_divisible_by_4():
    for year in (401, 2017, 2018, 2019):
        assert is_leap_year(year) == False
