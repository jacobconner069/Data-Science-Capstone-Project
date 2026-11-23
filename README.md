# SpaceX Falcon 9 First-Stage Landing Prediction

## Project Overview

This repository contains a data science capstone project that investigates whether the success of a SpaceX Falcon 9 first-stage landing can be predicted using historical launch data.

Recovering and reusing the first stage of a Falcon 9 rocket can reduce launch costs. The goal of this project is to explore the factors associated with landing outcomes and build classification models that predict whether a first-stage landing will be successful.

The project follows a data science workflow that includes data collection, data cleaning, exploratory data analysis (EDA), SQL analysis, geographic visualization, an interactive dashboard, and machine learning.

## Research Question

**Can we predict whether a SpaceX Falcon 9 first-stage landing will be successful using historical launch data?**

## Project Workflow

1. **Data collection** – Retrieve SpaceX launch information through the SpaceX API and collect historical launch records through web scraping.
2. **Data wrangling** – Inspect the data, address missing values, select relevant fields, and create a landing-outcome target variable.
3. **Exploratory data analysis** – Examine relationships between launch outcomes and variables such as flight number, launch site, payload mass, and orbit type.
4. **SQL analysis** – Use SQL queries to investigate launch sites, payload masses, landing outcomes, booster versions, and launch history.
5. **Data visualization** – Create static charts and interactive geographic maps to explore launch patterns and launch-site locations.
6. **Dashboard development** – Build a Plotly Dash application that lets users explore launch outcomes by launch site and payload mass.
7. **Predictive modeling** – Train and compare classification models to predict first-stage landing outcomes.

## Repository Contents

| File | Description |
|---|---|
| `DS-Capstone-Presentation.pdf` | Final project presentation describing the research question, methodology, visualizations, and findings. |
| `Data-Collection.ipynb` | Collects SpaceX launch information using API requests, processes the returned data, and prepares launch records for analysis. |
| `Webscraping.ipynb` | Uses `requests` and `BeautifulSoup` to extract historical Falcon 9 and Falcon Heavy launch records from a Wikipedia page and convert them into a Pandas DataFrame. |
| `Data-Wrangling.ipynb` | Inspects and cleans the launch dataset, explores missing values and launch outcomes, and creates the landing-success label used for prediction. |
| `Data-Visualization.ipynb` | Performs exploratory data analysis and feature engineering. Includes visualizations involving flight number, launch site, payload mass, orbit type, and yearly launch success. |
| `SQL-EDA.ipynb` | Uses SQL queries with a SQLite database to examine launch sites, payload masses, booster versions, and landing outcomes. |
| `Folium-Visuals.ipynb` | Creates interactive maps of launch sites and launch outcomes, and explores distances between launch sites and nearby geographic features. |
| `Dash-App.py` | Runs an interactive Plotly Dash dashboard with a launch-site dropdown, a payload-mass range slider, a success pie chart, and a payload-versus-outcome scatter plot. |
| `README.md` | Project documentation and setup instructions. |

## Technologies and Libraries

The project uses the following tools and Python libraries:

- **Python** – Main programming language.
- **Jupyter Notebook** – Data collection, cleaning, analysis, visualization, and modeling.
- **Pandas and NumPy** – Data manipulation and numerical operations.
- **Matplotlib and Seaborn** – Exploratory data visualizations.
- **Requests and BeautifulSoup** – API requests and web scraping.
- **SQLite and SQL** – Relational data storage and exploratory queries.
- **Folium** – Interactive geographic maps.
- **Plotly and Dash** – Interactive dashboard and charts.
- **Scikit-learn** – Classification, preprocessing, model selection, and evaluation.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/jacobconner069/Data-Science-Capstone-Project.git
cd Data-Science-Capstone-Project
```

### 2. Create and activate a virtual environment (recommended)

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

Install the main libraries used throughout the notebooks and dashboard:

```bash
pip install pandas numpy matplotlib seaborn requests beautifulsoup4 scikit-learn folium dash plotly sqlalchemy ipython-sql prettytable
```

Some notebooks may contain additional notebook-specific setup or package-version requirements. If a notebook reports a missing package, install that package in the active environment.

### 4. Start Jupyter Notebook

```bash
jupyter notebook
```

Open the notebook you want to run from the Jupyter interface.

## Running the Interactive Dashboard

The dashboard is implemented in `Dash-App.py`.

1. Make sure the dashboard dependencies are installed.
2. Open a terminal in the repository directory.
3. Run:

```bash
python Dash-App.py
```

The script downloads the dashboard dataset from the IBM Skills Network-hosted CSV source and saves it locally as `spacex_launch_dash.csv`. It then starts the Dash development server. Open the local address printed in the terminal (typically `http://127.0.0.1:8050`) in a web browser.

### Dashboard Features

- **Launch-site dropdown:** Select an individual launch site or view all sites.
- **Success pie chart:** View successful launch counts across all sites or the success/failure distribution for a selected site.
- **Payload range slider:** Filter launches by payload mass in kilograms.
- **Payload-versus-outcome scatter plot:** Explore landing outcomes across payload masses, with booster version category shown by color.

The dashboard requires an internet connection to retrieve its source CSV when it runs.

## Project Findings

The final presentation reports the following conclusions from the project's analysis:

- Landing success rates increased over time, suggesting improvements in rocket design and the landing/recovery process.
- Launch site, payload mass, and orbit type were identified as important factors to examine when studying landing outcomes.
- Several classification algorithms were trained and compared, including Logistic Regression, Support Vector Machine (SVM), Decision Tree, and K-Nearest Neighbors (KNN).
- The presentation reports that **K-Nearest Neighbors achieved the highest test accuracy at approximately 83%** among the models compared.

These findings are the results reported in the project presentation and should be interpreted in the context of the dataset, feature selection, and train/test split used in the notebooks.

## Data Sources

The notebooks retrieve or reference data from external sources, including:

- **SpaceX API:** Launch records and related launch information used during data collection.
- **Wikipedia – List of Falcon 9 and Falcon Heavy launches:** Historical launch records used in the web-scraping notebook. The notebook references a historical page snapshot dated June 9, 2021.
- **IBM Skills Network datasets:** CSV datasets used in several of the course-based analysis, visualization, mapping, and modeling notebooks.

Some datasets are downloaded when the notebooks or dashboard execute rather than being stored directly in this repository. Running those steps therefore requires an internet connection, and external data URLs may change or become unavailable.

## Notes

- Run the notebooks in the general project order shown in the **Project Workflow** section.
- Some notebooks are based on IBM Applied Data Science Capstone course labs and retain course-provided instructions and references.
- Notebook outputs and results may depend on the versions of the external datasets available when the notebooks are executed.
- The dashboard script creates `spacex_launch_dash.csv` in the working directory when it downloads the data.

## Author

**Jacob Conner**

## Course

IBM Applied Data Science Capstone (Coursera)

