from data_loader import DataLoader
from data_processor import DataProcessor
from analysis import SalesAnalyzer
from visualizations import Visualizer
import json
import os

def run_analysis():
    # Create output directory if it doesn't exist
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    # Load data
    data_path = os.getenv('DATA_PATH', './data/Pharma_Drug_Sales.csv')
    loader = DataLoader(data_path)
    data = loader.load_data()

    # Process data
    processor = DataProcessor(data)
    metrics = processor.calculate_revenue_metrics()
    company_w_analysis = processor.analyze_company_w()
    sales_allocation = processor.analyze_sales_allocation()

    # Analyze sales
    analyzer = SalesAnalyzer(data)
    forecast = analyzer.forecast_revenue_2025()
    factors = analyzer.identify_key_factors()
    recommendations = analyzer.recommend_focus_areas()

    # Generate report
    report = {
        'forecast_2025': forecast,
        'key_factors': {
            'price_elasticity': float(factors['price_elasticity']),
            'top_region': factors['regional_impact'].index[0],
            'top_channel': factors['channel_impact'].index[0]
        },
        'recommendations': recommendations,
        'current_metrics': {
            'total_revenue': float(metrics['total_revenue']),
            'top_drug': metrics['revenue_by_drug'].index[0]
        }
    }

    # Save report
    with open(os.path.join(output_dir, 'analysis_report.json'), 'w') as f:
        json.dump(report, f, indent=4)

    # Create visualizations
    viz = Visualizer(data)
    trends = viz.create_revenue_trends()
    company_analysis_viz = viz.create_company_w_analysis(company_w_analysis)

    # Save visualizations
    trends['revenue_trend'].write_html(os.path.join(output_dir, 'revenue_trend.html'))
    trends['revenue_by_region'].write_html(os.path.join(output_dir, 'revenue_by_region.html'))
    company_analysis_viz['drug_performance'].write_html(os.path.join(output_dir, 'drug_performance.html'))
    company_analysis_viz['channel_performance'].write_html(os.path.join(output_dir, 'channel_performance.html'))

if __name__ == "__main__":
    run_analysis() 