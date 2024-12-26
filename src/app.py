from flask import Flask, render_template, jsonify, send_file
from data_loader import DataLoader
from data_processor import DataProcessor
from analysis import SalesAnalyzer
from visualizations import Visualizer
import json
import os
import pandas as pd
from datetime import datetime
import glob

app = Flask(__name__)

def cleanup_old_files(output_dir: str, pattern: str) -> None:
    """Delete old export files matching the pattern"""
    files = glob.glob(os.path.join(output_dir, pattern))
    for file in files:
        try:
            os.remove(file)
        except Exception as e:
            app.logger.warning(f"Failed to delete {file}: {e}")

def cleanup_after_send(file_path: str):
    """Delete file after it's been sent"""
    try:
        os.remove(file_path)
    except Exception as e:
        app.logger.warning(f"Failed to delete {file_path}: {e}")

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

def generate_export_data(analysis_results):
    """Generate data for export"""
    # Create summary data
    summary_data = {
        'Metric': [
            'Forecast Revenue 2025',
            'Expected Growth',
            'Current Revenue',
            'Recommended Region',
            'Recommended Channel',
            'Recommended Drug',
        ],
        'Value': [
            f"${analysis_results['forecast']['forecast_2025']:,.2f}",
            f"{analysis_results['forecast']['expected_growth']:.1f}%",
            f"${analysis_results['forecast']['current_revenue']:,.2f}",
            analysis_results['recommendations']['recommended_regions'],
            analysis_results['recommendations']['recommended_channels'],
            analysis_results['recommendations']['recommended_drugs'],
        ]
    }
    return pd.DataFrame(summary_data)

@app.route('/')
def index():
    analysis_results = run_analysis()
    return render_template('index.html', results=analysis_results)

@app.route('/api/analysis')
def get_analysis():
    analysis_results = run_analysis()
    return jsonify(analysis_results)

@app.route('/export/<format>')
def export_report(format):
    """Export report in specified format"""
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Clean up old files before creating new ones
    cleanup_old_files(output_dir, 'pharma_analysis_report_*.*')
    
    analysis_results = run_analysis()
    df = generate_export_data(analysis_results)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    if format == 'excel':
        output_path = os.path.join(output_dir, f'pharma_analysis_report_{timestamp}.xlsx')
        df.to_excel(output_path, index=False, sheet_name='Analysis Summary')
        
        # Return file and ensure cleanup after sending
        response = send_file(
            output_path,
            as_attachment=True,
            download_name=f'pharma_analysis_report_{timestamp}.xlsx'
        )
        response.call_on_close(lambda: cleanup_after_send(output_path))
        return response
    
    elif format == 'csv':
        output_path = os.path.join(output_dir, f'pharma_analysis_report_{timestamp}.csv')
        df.to_csv(output_path, index=False)
        
        # Return file and ensure cleanup after sending
        response = send_file(
            output_path,
            as_attachment=True,
            download_name=f'pharma_analysis_report_{timestamp}.csv'
        )
        response.call_on_close(lambda: cleanup_after_send(output_path))
        return response
    
    return jsonify({'error': 'Invalid format'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8501) 