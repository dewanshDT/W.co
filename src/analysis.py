import pandas as pd
from typing import Dict, Any
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class SalesAnalyzer:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def forecast_revenue_2025(self) -> Dict[str, Any]:
        """Forecast revenue for 2025 using historical data"""
        # Create time-based features
        monthly_revenue = self.data.groupby(pd.Grouper(key='Sale Date', freq='M'))['Revenue'].sum().reset_index()
        monthly_revenue['month_number'] = range(len(monthly_revenue))
        
        # Prepare data for forecasting
        X = monthly_revenue[['month_number']]
        y = monthly_revenue['Revenue']
        
        # Train model
        model = LinearRegression()
        model.fit(X, y)
        
        # Forecast for 2025
        future_months = np.array(range(len(monthly_revenue), len(monthly_revenue) + 12)).reshape(-1, 1)
        forecast_2025 = model.predict(future_months)
        
        expected_growth = ((forecast_2025.sum() - y.sum()) / y.sum()) * 100
        
        return {
            'forecast_2025': forecast_2025.sum(),
            'expected_growth': expected_growth,
            'current_revenue': y.sum()
        }

    def identify_key_factors(self) -> Dict[str, Any]:
        """Identify factors impacting revenue"""
        correlations = {}
        
        # Analyze impact of pricing (using Units Sold as proxy)
        price_elasticity = np.corrcoef(self.data['Units Sold'], self.data['Revenue'])[0,1]
        
        # Analyze regional impact
        regional_impact = self.data.groupby('Region')['Revenue'].mean().sort_values(ascending=False)
        
        # Analyze channel impact
        channel_impact = self.data.groupby('Channel')['Revenue'].mean().sort_values(ascending=False)
        
        return {
            'price_elasticity': price_elasticity,
            'regional_impact': regional_impact,
            'channel_impact': channel_impact
        }

    def recommend_focus_areas(self) -> Dict[str, Any]:
        """Recommend focus areas for Company W"""
        company_w = self.data[self.data['Manufacturer'] == 'Company W']
        
        # Best performing regions
        top_regions = company_w.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
        
        # Best performing channels
        top_channels = company_w.groupby('Channel')['Revenue'].sum().sort_values(ascending=False)
        
        # Best performing drugs
        top_drugs = company_w.groupby('Drug Name')['Revenue'].sum().sort_values(ascending=False)
        
        return {
            'recommended_regions': top_regions.index[0],
            'recommended_channels': top_channels.index[0],
            'recommended_drugs': top_drugs.index[0]
        } 