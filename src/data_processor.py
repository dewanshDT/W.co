import pandas as pd
from typing import Dict, Any

class DataProcessor:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def calculate_revenue_metrics(self) -> Dict[str, Any]:
        """Calculate key revenue metrics"""
        total_revenue = self.data['Revenue'].sum()
        revenue_by_drug = self.data.groupby('Drug Name')['Revenue'].sum().sort_values(ascending=False)
        revenue_by_region = self.data.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
        revenue_by_channel = self.data.groupby('Channel')['Revenue'].sum().sort_values(ascending=False)

        return {
            'total_revenue': total_revenue,
            'revenue_by_drug': revenue_by_drug,
            'revenue_by_region': revenue_by_region,
            'revenue_by_channel': revenue_by_channel
        }

    def analyze_company_w(self) -> Dict[str, Any]:
        """Analyze Company W's performance"""
        company_w_data = self.data[self.data['Manufacturer'] == 'Company W']
        current_revenue = company_w_data['Revenue'].sum()
        
        # Calculate growth factors
        revenue_by_drug = company_w_data.groupby('Drug Name')['Revenue'].sum()
        revenue_by_region = company_w_data.groupby('Region')['Revenue'].sum()
        revenue_by_channel = company_w_data.groupby('Channel')['Revenue'].sum()

        return {
            'current_revenue': current_revenue,
            'revenue_by_drug': revenue_by_drug,
            'revenue_by_region': revenue_by_region,
            'revenue_by_channel': revenue_by_channel
        }

    def analyze_sales_allocation(self) -> pd.DataFrame:
        """Analyze optimal sales representative allocation"""
        sales_performance = self.data.groupby(['Region', 'Channel', 'Drug Name'])['Revenue'].sum().reset_index()
        return sales_performance.sort_values('Revenue', ascending=False) 