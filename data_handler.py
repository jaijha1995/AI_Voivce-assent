import pandas as pd

class CSVDataHandler:
    def __init__(self, path):
        self.path = path
        self.data = self._load_data()

    def _load_data(self):
        try:
            return pd.read_csv(self.path)
        except Exception as e:
            print(f"[Data Error] {e}")
            return pd.DataFrame()

    def describe(self):
        return self.data.describe().to_string()

    def get_sample(self, rows=5):
        return self.data.head(rows).to_string(index=False)

    def get_columns(self):
        return ", ".join(self.data.columns)
