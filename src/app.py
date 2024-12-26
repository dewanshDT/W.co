from flask import Flask, render_template, jsonify
from data_loader import DataLoader
from data_processor import DataProcessor
from analysis import SalesAnalyzer
from visualizations import Visualizer
import json
import os

app = Flask(__name__)

def run_analysis():
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    data_path = os.getenv('DATA_PATH', './data/Pharma_Drug_Sales.csv')
    loader = DataLoader(data_path)
    data = loader.load_data()
    
    processor = DataProcessor(data)
    metrics = processor.calculate_revenue_metrics()
    company_w_analysis = processor.analyze_company_w()
    
    analyzer = SalesAnalyzer(data)
    forecast = analyzer.forecast_revenue_2025()
    factors = analyzer.identify_key_factors()
    recommendations = analyzer.recommend_focus_areas()
    
    viz = Visualizer(data)
    trends = viz.create_revenue_trends()
    company_analysis_viz = viz.create_company_w_analysis(company_w_analysis)
    
    # Convert Plotly figures to JSON
    visualizations = {
        'revenue_trend': trends['revenue_trend'].to_json(),
        'revenue_by_region': trends['revenue_by_region'].to_json(),
        'drug_performance': company_analysis_viz['drug_performance'].to_json(),
        'channel_performance': company_analysis_viz['channel_performance'].to_json()
    }
    
    return {
        'metrics': metrics,
        'forecast': forecast,
        'factors': factors,
        'recommendations': recommendations,
        'visualizations': visualizations
    }

@app.route('/')
def index():
    analysis_results = run_analysis()
    return render_template('index.html', results=analysis_results)

@app.route('/api/analysis')
def get_analysis():
    analysis_results = run_analysis()
    return jsonify(analysis_results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8501) 