import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, Any
import pandas as pd

class Visualizer:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def create_revenue_trends(self) -> Dict[str, Any]:
        """Create revenue trend visualizations"""
        # Revenue over time
        revenue_trend = px.line(
            self.data.groupby('Sale Date')['Revenue'].sum().reset_index(),
            x='Sale Date',
            y='Revenue',
            title='Revenue Trend Over Time'
        )

        # Revenue by region
        revenue_by_region = px.bar(
            self.data.groupby('Region')['Revenue'].sum().reset_index(),
            x='Region',
            y='Revenue',
            title='Revenue by Region'
        )

        return {
            'revenue_trend': revenue_trend,
            'revenue_by_region': revenue_by_region
        }

    def create_company_w_analysis(self, analysis_results: Dict[str, Any]) -> Dict[str, Any]:
        """Create visualizations for Company W analysis"""
        company_w_data = self.data[self.data['Manufacturer'] == 'Company W']
        
        # Performance by drug
        drug_performance = px.pie(
            company_w_data.groupby('Drug Name')['Revenue'].sum().reset_index(),
            values='Revenue',
            names='Drug Name',
            title='Revenue Distribution by Drug (Company W)'
        )

        # Channel performance
        channel_performance = px.bar(
            company_w_data.groupby('Channel')['Revenue'].sum().reset_index(),
            x='Channel',
            y='Revenue',
            title='Revenue by Channel (Company W)'
        )

        return {
            'drug_performance': drug_performance,
            'channel_performance': channel_performance
        } 