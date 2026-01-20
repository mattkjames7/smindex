import sqlite3


create_schema = [
    """
    -- Table to store SMI data paths by date
    CREATE TABLE IF NOT EXISTS smi_data (
        id INTEGER PRIMARY KEY,
        date INTEGER,
        path TEXT
    );
    """,
    """
    -- Index on date for faster queries
    CREATE INDEX IF NOT EXISTS idx_date ON smi_data (date);
    """,
    """
    -- Table to store substorm event data
    CREATE TABLE IF NOT EXISTS substorms (
        id INTEGER PRIMARY KEY,
        date INTEGER,
        ut REAL,
        timestamp REAL,
        mlt REAL,
        mlat REAL,
        glon REAL,
        glat REAL,
        source TEXT
    );
    """,
    """
    -- Index on date for substorms table
    CREATE INDEX IF NOT EXISTS idx_substorm_date ON substorms (date);
    """
]


class SMIDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.initialize()

    def initialize(self):
        for item in create_schema:
            self.cursor.execute(item)
        self.conn.commit()

    def get_date(self, date):
        date = int(date)
        self.cursor.execute("SELECT path FROM smi_data WHERE date=?", (date,))
        result = self.cursor.fetchone()
        print(result)
        return result[0] if result else None

    def insert_date(self, date, path):
        date = int(date)
        if self.get_date(date) is not None:
            self.overwrite_date(date, path)
            return
        self.cursor.execute(
            "INSERT INTO smi_data (date, path) VALUES (?, ?)", (date, path)
        )
        self.conn.commit()

    def overwrite_date(self, date, path):
        date = int(date)
        path = str(path)
        self.cursor.execute(
            "UPDATE smi_data SET path = ? WHERE date = ?", (path, date)
        )
        self.conn.commit()

    def check_existing_dates(self, dates):
        dates = [int(d) for d in dates]
        placeholders = ','.join("?" for _ in dates)
        query = f"SELECT date FROM smi_data WHERE date IN ({placeholders})"
        print(query)
        self.cursor.execute(query, dates)
        results = self.cursor.fetchall()
        print(results)
        return {row[0] for row in results}
    
    def insert_substorms(self, data):
        sql = """
            INSERT INTO substorms
            (date, ut, timestamp, mlt, mlat, glon, glat, source)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        rows = [
            (
                int(row['date']),
                float(row['ut']),
                float(row['timestamp']),
                float(row['mlt']),
                float(row['mlat']),
                float(row['glon']),
                float(row['glat']),
                str(row['source']),
            )
            for row in data
        ]

        self.cursor.executemany(sql, rows)
        self.conn.commit()

    def read_substorms(self, start_date=None, end_date=None):
        if start_date and end_date:
            self.cursor.execute(
                "SELECT * FROM substorms WHERE date BETWEEN ? AND ?",
                (start_date, end_date)
            )
        elif start_date:
            self.cursor.execute(
                "SELECT * FROM substorms WHERE date >= ?",
                (start_date,)
            )
        elif end_date:
            self.cursor.execute(
                "SELECT * FROM substorms WHERE date <= ?",
                (end_date,)
            )
        else:
            self.cursor.execute("SELECT * FROM substorms")
        rows = self.cursor.fetchall()
        return rows
