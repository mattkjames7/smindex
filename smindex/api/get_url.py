from datetime import datetime
from typing import List


def get_index_url(username: str, start_time: datetime | List[int] | str, duration: int | float):
    print(username, start_time, duration)
    if isinstance(start_time, list):
        start_time = datetime(*start_time)
    start = datetime.strftime(start_time, "%Y-%m-%dT%H:%M")

    url = "https://supermag.jhuapl.edu/services/indices.php?python&nohead"
    url += f"&start={start}&logon={username}&extent={duration:012d}"

    fields = [
        "sme",
        "sml",
        "smu",
        "num",
        "mlat",
        "mlt",
        "glat",
        "glon",
        "smer",
        "smlr",
        "smur",
        "numr",
        "mlatr",
        "mltr",
        "glatr",
        "glonr",
        "smr",
        "ltsmr",
        "ltnum",
        "nsmr"
    ]

    return url + "&indices=" + ",".join(fields)


def get_substorm_url(
    username: str,
    start_time: datetime | List[int] | str,
    end_time: datetime | List[int] | str,
    list_type: str = "newell"
):

    valid_list_types = ["newell", "liou", "frey", "ohtani", "forsyth"]
    if list_type not in valid_list_types:
        raise ValueError(f"list_type must be one of {valid_list_types}")

    fmt = "csv"

    if isinstance(start_time, list):
        start_time = datetime(*start_time)
    start = datetime.strftime(start_time, "%Y-%m-%dT%H:%M:%S.000Z")

    if isinstance(end_time, list):
        end_time = datetime(*end_time)
    end = datetime.strftime(end_time, "%Y-%m-%dT%H:%M:%S.000Z")

    url = "https://supermag.jhuapl.edu/lib/services/?service=substorms"
    url += f"&downloadtype=substorm_list&user={username}&fmt={fmt}&start={start}&end={end}&list={list_type}"

    return url

"""
can do 25 years, it seems
for substorms:
https://supermag.jhuapl.edu/lib/services/?service=substorms&downloadtype=substorm_list&user=mj102&fmt=ascii&start=2001-01-01T00:00:00.000Z&end=2001-01-02T00:00:00.000Z&list=newell
https://supermag.jhuapl.edu/lib/services/?service=substorms&downloadtype=substorm_list&user=mj102&fmt=ascii&start=2001-01-01T00:00:00.000Z&end=2002-01-02T00:00:00.000Z&list=newell
https://supermag.jhuapl.edu/lib/services/?service=substorms&downloadtype=substorm_list&user=mj102&fmt=csv&start=2001-01-01T00:00:00.000Z&end=2001-01-01T23:59:00.000Z&list=liou
https://supermag.jhuapl.edu/lib/services/?service=substorms&downloadtype=substorm_list&user=mj102&fmt=csv&start=2001-01-01T00:00:00.000Z&end=2001-01-01T23:59:00.000Z&list=frey
https://supermag.jhuapl.edu/lib/services/?service=substorms&downloadtype=substorm_list&user=mj102&fmt=csv&start=2001-01-01T00:00:00.000Z&end=2001-01-01T23:59:00.000Z&list=ohtani
https://supermag.jhuapl.edu/lib/services/?service=substorms&downloadtype=substorm_list&user=mj102&fmt=csv&start=2001-01-01T00:00:00.000Z&end=2001-01-01T23:59:00.000Z&list=forsyth
"""