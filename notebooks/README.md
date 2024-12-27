# Pharma Sales Analysis - Jupyter Guide

This guide explains how to run the pharmaceutical sales analysis using Jupyter Notebook locally.

## Prerequisites

1. Python 3.8 or higher
2. pip (Python package installer)
3. Jupyter Notebook

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd pharma-sales-analysis
```

2. Create and activate a virtual environment:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
pip install jupyter  # Install Jupyter if not already installed
```

## Running the Analysis

1. Make sure your virtual environment is activated
2. Navigate to the project root directory
3. Start Jupyter Notebook:

```bash
jupyter notebook
```

4. In the Jupyter interface, navigate to `notebooks` folder
5. Open `Pharma_Analysis.ipynb`

## Project Structure

```
pharma-sales-analysis/
├── notebooks/
│   ├── Pharma_Analysis.ipynb
│   └── README.md (this file)
├── src/
│   ├── data_loader.py
���   ├── data_processor.py
│   ├── analysis.py
│   └── visualizations.py
├── data/
│   └── Pharma_Drug_Sales.csv
└── requirements.txt
```

## Analysis Steps

The notebook contains the following sections:

1. Data Loading and Preprocessing
2. Revenue Analysis
3. Forecasting
4. Visualization
5. Recommendations

## Troubleshooting

1. Module Import Issues:

   - Ensure you're running Jupyter from the project root directory
   - Check if all dependencies are installed:

   ```bash
   pip list | grep -E "pandas|numpy|scikit-learn|plotly"
   ```

2. Data Loading Issues:

   - Verify the data file exists in the data directory
   - Check file permissions
   - Ensure correct file path in the notebook

3. Visualization Problems:

   - Make sure plotly is installed:

   ```bash
   pip install plotly --upgrade
   ```

   - Try restarting the kernel: Kernel → Restart

## Tips

1. Running Cells:

   - Use Shift + Enter to run a cell and move to the next
   - Use Ctrl + Enter to run a cell and stay on it

2. Saving Work:

   - Notebook autosaves every few minutes
   - Use Ctrl + S to save manually

3. Best Practices:
   - Run cells in order
   - Restart kernel and run all if you make changes to source files
   - Use markdown cells for documentation

## Getting Help

If you encounter issues:

1. Check the error message carefully
2. Verify all prerequisites are installed
3. Ensure you're in the correct directory
4. Try restarting the kernel and running all cells

## Additional Resources

- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)
- [Plotly Python Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
