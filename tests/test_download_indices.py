import smindex
import datetime


def test_download_indices_single_int_date():
    """
    Test downloading a single day's worth of indices using an integer date.
    1440 minutes in a day, so expect 1440 entries.
    """

    date = 20250101
    data = smindex.indices(date)

    assert len(data) == 1440
    assert all(data.date == date)


def test_download_indices_int_date_range():
    """
    Test downloading indices over a range of integer dates.
    Expect 3 days * 1440 minutes = 4320 entries.
    """

    start_date = 20250103
    end_date = 20250105
    all_data = smindex.indices(start_date, end_date)

    expected_length = 3 * 1440
    assert len(all_data) == expected_length
    assert all(all_data.date >= start_date)
    assert all(all_data.date <= end_date)


def test_download_indices_datetime_range():
    """
    Test downloading indices over a range of datetime objects.
    Expect total minutes from start to end datetime.
    """

    start = datetime.datetime(2025, 2, 1, 0, 0)
    end = datetime.datetime(2025, 2, 2, 23, 45)

    days = 1
    hours = 23
    minutes = 45
    total_minutes = (days * 24 * 60) + (hours * 60) + minutes + 1

    all_data = smindex.indices(start, end)
    assert len(all_data) == total_minutes
    assert all(
        ((all_data.date >= 20250201) & (all_data.ut >= 0.0)) |
        ((all_data.date <= 20250202) & (all_data.ut <= 23.75))
    )


def test_download_indices_mixed_range():
    """
    Test downloading indices over a mixed range of integer date with time and datetime object.
    Expect total minutes from start to end datetime.
    """

    start = (20250310, 12.0)
    end = datetime.datetime(2025, 3, 11, 18, 0)

    total_minutes = (12 * 60) + (18 * 60) + 1

    all_data = smindex.indices(start, end)
    assert len(all_data) == total_minutes
    assert all(
        (all_data.date == 20250310) & (all_data.ut >= 12.0) |
        (all_data.date == 20250311) & (all_data.ut <= 18.0)
    )
