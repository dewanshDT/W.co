# Pharma Sales Analysis Project

This project analyzes pharmaceutical sales data to help Company W achieve their 20% revenue growth target in 2025.

## Project Structure

- `data/`: Contains the raw data files
  - `Pharma_Drug_Sales.csv`: Main dataset
- `src/`: Source code for data processing and analysis
  - `data_loader.py`: Handles data loading and preprocessing
  - `data_processor.py`: Processes and transforms data
  - `analysis.py`: Core analysis logic
  - `visualizations.py`: Creates visualizations
  - `app.py`: Flask web application
  - `templates/`: HTML templates for web interface
- `output/`: Generated analysis results and visualizations
- `Dockerfile`: Docker configuration
- `docker-compose.yml`: Docker Compose configuration

## Key Features

1. Revenue forecasting for 2025
2. Analysis of factors impacting revenue
3. Recommendations for regional, channel, and drug focus
4. Sales representative allocation analysis
5. Interactive web dashboard

## Running with Docker (Recommended)

### Prerequisites

- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Docker Compose installed ([Get Docker Compose](https://docs.docker.com/compose/install/))

### Steps to Run

1. Clone the repository:

```bash
git clone <repository-url>
cd pharma-sales-analysis
```

2. Build and run in one command:

```bash
docker-compose up --build
```

3. Access the web interface:
   Open your browser and navigate to:

```bash
http://localhost:8501
```

### Managing the Application

1. View logs:

```bash
docker-compose logs -f
```

2. Stop the application:

```bash
docker-compose down
```

3. Rebuild after changes:

```bash
docker-compose up --build
```

## Web Interface Features

The dashboard provides:

1. Revenue Metrics

   - Forecast for 2025
   - Expected growth percentage
   - Current revenue status

2. Focus Area Recommendations

   - Recommended regions
   - Channel strategy
   - Drug focus areas

3. Interactive Visualizations
   - Revenue trends
   - Regional performance
   - Drug performance analysis
   - Channel distribution

## Troubleshooting

1. Port Issues:

```bash
# Check if port 8501 is in use
netstat -an | grep 8501  # Linux/Mac
netstat -an | findstr 8501  # Windows
```

2. Container Issues:

```bash
# View container logs
docker-compose logs -f

# Check container status
docker ps -a
```

3. Access Issues:

- Ensure firewall allows access to port 8501
- Try accessing using different browsers
- Check if Docker is running properly

## Directory Structure

```
pharma-sales-analysis/
├── data/
│   └── Pharma_Drug_Sales.csv
├── src/
│   ├── data_loader.py
│   ├── data_processor.py
│   ├── analysis.py
│   ├── visualizations.py
│   ├── app.py
│   └── templates/
│       └── index.html
├── output/
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Cleaning Up

```bash
# Stop and remove containers
docker-compose down

# Remove all unused containers and volumes
docker-compose down -v
docker system prune
```

## Analysis Methodology & Principles

### 1. Data Processing Pipeline

The analysis follows a structured pipeline approach:

1. **Data Loading** (`data_loader.py`)

   - Handles raw data ingestion
   - Performs initial data cleaning
   - Converts data types (dates, currency values)

2. **Data Processing** (`data_processor.py`)

   - Calculates key revenue metrics
   - Groups data by different dimensions
   - Analyzes Company W's specific performance

3. **Advanced Analysis** (`analysis.py`)

   - Revenue forecasting using linear regression
   - Key factor identification
   - Focus area recommendations

4. **Visualization** (`visualizations.py`)
   - Interactive trend analysis
   - Performance comparisons
   - Distribution analysis

### 2. Key Analysis Components

#### Revenue Forecasting

- Uses historical data to predict 2025 revenue
- Employs linear regression for trend analysis
- Considers monthly revenue patterns
- Calculates expected growth percentage

#### Performance Analysis

- Regional performance evaluation
- Channel effectiveness analysis
- Drug portfolio assessment
- Sales representative allocation optimization

#### Impact Analysis

- Price elasticity evaluation
- Regional impact assessment
- Channel effectiveness measurement
- Product performance metrics

### 3. Design Principles

1. **Modularity**

   - Separate modules for different functionalities
   - Easy to maintain and extend
   - Clear separation of concerns

2. **Data-Driven Decision Making**

   - All recommendations based on statistical analysis
   - Quantitative metrics for performance
   - Evidence-based growth strategies

3. **Scalability**

   - Designed to handle growing data volumes
   - Efficient data processing methods
   - Optimized database operations

4. **Visualization First**
   - Interactive dashboards for better insights
   - Clear visual representation of trends
   - Easy-to-understand metrics presentation

### 4. Export Functionality

The system provides two export formats:

1. **Excel Export**

   - Comprehensive analysis summary
   - Formatted worksheets
   - Key metrics and recommendations

2. **CSV Export**
   - Raw data export
   - Compatible with other analysis tools
   - Easy to integrate with other systems

### 5. Implementation Best Practices

1. **Code Organization**

   - Clear file structure
   - Consistent naming conventions
   - Well-documented functions

2. **Error Handling**

   - Robust data validation
   - Clear error messages
   - Graceful failure handling

3. **Performance Optimization**

   - Efficient data processing
   - Optimized database queries
   - Caching where appropriate

4. **Security**
   - Secure file handling
   - Protected API endpoints
   - Safe data export
