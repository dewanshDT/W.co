import pandas as pd
from typing import Dict, Any, List
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

    def analyze_competitors(self) -> Dict[str, Any]:
        """Analyze competitor performance and market dynamics"""
        # Market share analysis
        total_market_revenue = self.data['Revenue'].sum()
        market_share = self.data.groupby('Manufacturer')['Revenue'].sum().sort_values(ascending=False)
        market_share_pct = (market_share / total_market_revenue * 100).round(2)

        # Growth rate by manufacturer
        manufacturer_growth = self.data.pivot_table(
            values='Revenue',
            index='Sale Date',
            columns='Manufacturer',
            aggfunc='sum'
        ).pct_change(periods=12).mean() * 100  # Annualized growth rate

        # Product portfolio analysis
        portfolio_diversity = self.data.groupby('Manufacturer')['Drug Name'].nunique().sort_values(ascending=False)

        # Channel strength analysis
        channel_strength = {}
        for manufacturer in self.data['Manufacturer'].unique():
            manufacturer_data = self.data[self.data['Manufacturer'] == manufacturer]
            channel_share = manufacturer_data.groupby('Channel')['Revenue'].sum()
            top_channel = channel_share.idxmax()
            channel_strength[manufacturer] = {
                'top_channel': top_channel,
                'channel_revenue': channel_share[top_channel]
            }

        # Regional dominance
        regional_dominance = {}
        for region in self.data['Region'].unique():
            region_data = self.data[self.data['Region'] == region]
            top_manufacturer = region_data.groupby('Manufacturer')['Revenue'].sum().idxmax()
            regional_dominance[region] = top_manufacturer

        return {
            'market_share': market_share_pct.to_dict(),
            'growth_rates': manufacturer_growth.to_dict(),
            'portfolio_diversity': portfolio_diversity.to_dict(),
            'channel_strength': channel_strength,
            'regional_dominance': regional_dominance
        }

    def get_competitive_advantages(self) -> Dict[str, List[str]]:
        """Identify competitive advantages and disadvantages for Company W"""
        company_w_data = self.data[self.data['Manufacturer'] == 'Company W']
        other_manufacturers = self.data[self.data['Manufacturer'] != 'Company W']

        # Price positioning analysis
        avg_price_w = company_w_data['Revenue'].sum() / company_w_data['Units Sold'].sum()
        avg_price_others = other_manufacturers['Revenue'].sum() / other_manufacturers['Units Sold'].sum()

        # Market presence
        w_regions = set(company_w_data['Region'].unique())
        w_channels = set(company_w_data['Channel'].unique())
        
        advantages = []
        disadvantages = []

        # Analyze pricing position
        if avg_price_w < avg_price_others:
            advantages.append("Competitive pricing advantage")
        else:
            disadvantages.append("Higher pricing compared to competitors")

        # Analyze market coverage
        total_regions = set(self.data['Region'].unique())
        if len(w_regions) == len(total_regions):
            advantages.append("Full regional market coverage")
        else:
            disadvantages.append(f"Limited presence in {len(total_regions) - len(w_regions)} regions")

        # Analyze channel efficiency
        w_channel_revenue = company_w_data.groupby('Channel')['Revenue'].mean()
        others_channel_revenue = other_manufacturers.groupby('Channel')['Revenue'].mean()
        
        strong_channels = w_channel_revenue[w_channel_revenue > others_channel_revenue].index.tolist()
        weak_channels = w_channel_revenue[w_channel_revenue < others_channel_revenue].index.tolist()

        if strong_channels:
            advantages.append(f"Strong performance in channels: {', '.join(strong_channels)}")
        if weak_channels:
            disadvantages.append(f"Underperforming in channels: {', '.join(weak_channels)}")

        return {
            'advantages': advantages,
            'disadvantages': disadvantages
        } 