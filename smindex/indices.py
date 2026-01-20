from ._globals import db, smi_dtype
from .download_indices import download_indices
import numpy as np
import datetime
import DateTimeTools as dtt
from tqdm import tqdm


def _normalize_date_input(date_input):

    has_time = False
    if isinstance(date_input, tuple):
        date, ut = date_input
        timestamp = dtt.UnixTime(date, ut)[0]
    elif isinstance(date_input, int):
        date = date_input
        ut = 0.0
        timestamp = dtt.UnixTime(date, ut)[0]
    elif isinstance(date_input, datetime.datetime):
        date = int(date_input.strftime("%Y%m%d"))
        timestamp = date_input.timestamp()
        has_time = True
    elif isinstance(date_input, np.datetime64):
        dt = date_input.astype('datetime64[us]').item()
        date = int(dt.strftime("%Y%m%d"))
        timestamp = dt.timestamp()
        has_time = True
    elif isinstance(date_input, datetime.date):
        date = int(date_input.strftime("%Y%m%d"))
        ut = 0.0
        timestamp = dtt.UnixTime(date, ut)[0]
    else:
        raise ValueError("Invalid input type for date")

    return date, timestamp, has_time


def indices(start, end=None, overwrite=False):
    """

    Input options:
    start =  datetime.date | int (YYYYMMDD) | datetime.datetime AND end = None -> single day of data
    start = datetime.date | int (YYYYMMDD)  AND end = datetime.date | int (YYYYMMDD) -> full days of data in whole range inclusive
    start AND/OR end are of type [datetime.datetime OR (int, float)] AND end is not None -> limit to within time range

    """

    # normalize inputs
    start_date, start_ts, start_has_time = _normalize_date_input(start)
    limit_time = False
    if end is not None:
        end_date, end_ts, end_has_time = _normalize_date_input(end)
        print(start_has_time, end_has_time)
        dates = dtt.ListDates(start_date, end_date)
        if start_has_time or end_has_time:
            limit_time = True
    else:
        dates = [start_date]

    # check which dates need to be downloaded
    existing_dates = db.check_existing_dates(dates)
    print(existing_dates)
    dates_to_download = [d for d in dates if (d not in existing_dates) or overwrite]

    if len(dates_to_download) > 0:
        for date in tqdm(dates_to_download, desc="Downloading SMI indices"):
            download_indices(date, overwrite=overwrite, quiet=False)

    # read in data
    all_data = []
    n = 0
    for date in dates:
        path = db.get_date(date)
        data = np.load(path)
        all_data.append(data)
        n += data.size

    data = np.recarray((n,), dtype=smi_dtype)
    pos = 0
    for day_data in all_data:
        data[pos:pos + day_data.size] = day_data
        pos += day_data.size

    if limit_time:
        print(start_ts, end_ts)
        mask = (data.timestamp >= start_ts) & (data.timestamp <= end_ts)
        data = data[mask]

    return data
