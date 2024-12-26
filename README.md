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
