# Workplace Mental Health — Mini Project

A small, extensible project for exploring and analyzing workplace mental health data. You can run it with the included **sample data** right away, then swap in a real dataset when you have one.

## What's in this repo

- **Sample data** (`data/sample_mental_health.csv`) — synthetic survey-style data so you can run the code without any external dataset.
- **Data loader** (`src/load_data.py`) — load CSV data; works with the sample file or your own.
- **Simple analysis** (`src/explore_data.py`) — basic stats and a few visualizations.
- **Requirements** — Python dependencies in `requirements.txt`.

## Quick start

### 1. Clone or create the project

```bash
cd workplace-mental-health
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run with sample data

```bash
python src/explore_data.py
```

This uses the sample CSV and prints summary stats; if you have a display, it will show simple plots.

## Using your own dataset

You don’t need a dataset to start — the sample data is enough. When you’re ready:

1. **Get a dataset** (see options below).
2. **Put your CSV** in `data/` (e.g. `data/mental_health_survey.csv`).
3. **Adjust column names** in `src/load_data.py` and `src/explore_data.py` to match your CSV (e.g. age, gender, work type, mental health questions).

### Where to find workplace mental health data

| Source | Description |
|--------|-------------|
| [OSMI Mental Health in Tech Survey (Kaggle)](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey) | Survey of tech workers; mental health and workplace attitudes. |
| [Remote Work and Mental Health (Kaggle)](https://www.kaggle.com/datasets/waqi786/remote-work-and-mental-health) | Remote work and mental health. |
| [OSMI 2017–2021 (Mendeley Data)](https://data.mendeley.com/datasets/mmnzx4w8cg/1) | Multi-year OSMI survey data. |

Download a CSV, place it in `data/`, and update the code to use your file and column names.

## Updating over time

- **Add new scripts** in `src/` (e.g. modeling, more visualizations).
- **Add notebooks** in a `notebooks/` folder for exploration.
- **Keep `data/` for CSVs** — add a `data/README.md` to note which files are sample vs real (and add `data/*.csv` to `.gitignore` for large files if you prefer).

## Pushing to GitHub

```bash
git init
git add .
git commit -m "Initial commit: workplace mental health mini project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/workplace-mental-health.git
git push -u origin main
```

Create the repo on GitHub first (empty, no README), then run the commands above. Use a `.gitignore` so you don’t commit `venv/`, `__pycache__/`, or large data files if you add them later.

## License

Use and adapt as you like. If you use a specific dataset, check its license (e.g. OSMI is often CC BY 4.0).
