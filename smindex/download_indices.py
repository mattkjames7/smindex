from ._globals import db, bindir
from . import api
from .convert_index_data import convert_index_data
import numpy as np
import os


def download_indices(date: int, overwrite: bool = False, quiet: bool = False) -> np.recarray:
    """
    Download SMI data for a specific date if not already present in the database.

    Inputs
    ======
    date : int
        Date in YYYYMMDD format.
    overwrite : bool, optional
        If True, overwrite existing data for the date. Default is False.

    Returns
    =======
    data : np.recarray
        Structured numpy recarray containing the index data for the specified date.
    """

    existing_entry = db.get_date(date)
    print(existing_entry)
    if existing_entry and not overwrite:
        if not quiet:
            print(f"Data for date {date} already exists. Skipping download.")
        return existing_entry[0]

    if not quiet:
        print(f"Downloading data for date {date}...")
    json_data = api.request_indices(date)
    data = convert_index_data(json_data)

    os.makedirs(bindir, exist_ok=True)
    filename = os.path.join(bindir, f"smi_{date}.npy")
    np.save(filename, data)

    db.insert_date(date, filename)

    return data
