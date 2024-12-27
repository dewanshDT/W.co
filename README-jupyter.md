# Pharma Sales Analysis - Jupyter Notebook Guide

This guide explains how to run the pharmaceutical sales analysis using Jupyter Notebook.

## Prerequisites

1. Python 3.8 or higher
2. Jupyter Notebook/Lab
3. Required packages (listed in requirements.txt)

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd pharma-sales-analysis
```

2. Create a virtual environment:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Unix/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
pip install jupyter  # Install Jupyter if not already installed
```

## Running the Analysis

1. Start Jupyter Notebook:

```bash
jupyter notebook
```

2. Create a new notebook in the project directory:

   - Click "New" → "Python 3"
   - Name it "Pharma_Analysis.ipynb"

3. Copy and run the following code blocks in separate cells:

```python
# Import required libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px
import plotly.graph_objects as go
import os

# Import project modules
from src.data_loader import DataLoader
from src.data_processor import DataProcessor
from src.analysis import SalesAnalyzer
from src.visualizations import Visualizer
```

```python
# Load and process data
loader = DataLoader('./data/Pharma_Drug_Sales.csv')
data = loader.load_data()

# Initialize processors
processor = DataProcessor(data)
analyzer = SalesAnalyzer(data)
visualizer = Visualizer(data)
```

```python
# Calculate metrics
metrics = processor.calculate_revenue_metrics()
company_w_analysis = processor.analyze_company_w()
sales_allocation = processor.analyze_sales_allocation()

print("Total Revenue:", f"${metrics['total_revenue']:,.2f}")
print("\nTop Drugs by Revenue:")
print(metrics['revenue_by_drug'].head())
```

```python
# Generate forecasts
forecast = analyzer.forecast_revenue_2025()
print("2025 Forecast:")
print(f"Forecast Revenue: ${forecast['forecast_2025']:,.2f}")
print(f"Expected Growth: {forecast['expected_growth']:.1f}%")
```

```python
# Create visualizations
trends = visualizer.create_revenue_trends()
company_analysis_viz = visualizer.create_company_w_analysis(company_w_analysis)

# Display plots
trends['revenue_trend'].show()
trends['revenue_by_region'].show()
company_analysis_viz['drug_performance'].show()
company_analysis_viz['channel_performance'].show()
```

## Analysis Components

### 1. Data Loading

- Loads CSV data
- Converts date and currency formats
- Performs initial data cleaning

### 2. Data Processing

- Calculates revenue metrics
- Analyzes Company W's performance
- Generates sales allocation recommendations

### 3. Analysis

- Revenue forecasting for 2025
- Key factor identification
- Focus area recommendations

### 4. Visualizations

- Revenue trends over time
- Regional performance analysis
- Drug performance distribution
- Channel performance analysis

## Saving Results

To save analysis results:

```python
# Create output directory
os.makedirs('output', exist_ok=True)

# Save metrics to CSV
pd.DataFrame(metrics['revenue_by_drug']).to_csv('output/revenue_by_drug.csv')
pd.DataFrame(metrics['revenue_by_region']).to_csv('output/revenue_by_region.csv')

# Save visualizations as HTML
trends['revenue_trend'].write_html('output/revenue_trend.html')
trends['revenue_by_region'].write_html('output/revenue_by_region.html')
company_analysis_viz['drug_performance'].write_html('output/drug_performance.html')
company_analysis_viz['channel_performance'].write_html('output/channel_performance.html')
```

## Tips for Jupyter Notebook

1. **Cell Execution**:

   - Use Shift+Enter to run a cell and move to the next one
   - Use Ctrl+Enter to run a cell and stay on it

2. **Markdown Cells**:

   - Use markdown cells for documentation
   - Add headers, lists, and explanations

3. **Interactive Plots**:

   - Plotly plots are interactive in Jupyter
   - Hover over data points for details
   - Use zoom and pan features

4. **Memory Management**:
   - Restart kernel if memory usage gets high
   - Clear output of cells not needed

## Troubleshooting

1. **Import Errors**:

   - Ensure you're in the correct directory
   - Check if all dependencies are installed
   - Verify Python path includes project directory

2. **Data Loading Issues**:

   - Verify data file path
   - Check CSV file format
   - Ensure proper file permissions

3. **Visualization Problems**:
   - Update plotly if plots don't display
   - Clear browser cache
   - Try different browsers

## Additional Analysis

Feel free to add more analysis cells:

- Custom visualizations
- Different time periods
- Specific drug analysis
- Regional comparisons
