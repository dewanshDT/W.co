import pandas as pd
from typing import Optional

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data: Optional[pd.DataFrame] = None

    def load_data(self) -> pd.DataFrame:
        """Load the CSV data into a pandas DataFrame"""
        self.data = pd.read_csv(self.file_path)
        
        # Convert Sale Date to datetime
        self.data['Sale Date'] = pd.to_datetime(self.data['Sale Date'])
        
        # Convert Revenue from string to float
        self.data['Revenue'] = self.data['Revenue'].str.replace('$', '').str.replace(',', '').astype(float)
        
        return self.data 