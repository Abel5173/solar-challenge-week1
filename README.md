# Solar Challenge Week 1

A project for learning Git, CI/CD, and exploratory data analysis (EDA) on solar and meteorological datasets from West Africa. This repository demonstrates best practices in code organization, reproducibility, and collaborative development using Git, CI/CD, and interactive dashboards.

---

## Project Overview

This repository contains:

- Data profiling, cleaning, and EDA for Benin, Sierra Leone, and Togo solar datasets.
- Cross-country comparison and statistical analysis.
- An interactive Streamlit dashboard for visualizing insights.
- Automated testing and CI/CD workflows.

---

## Directory Structure

```
.
├── .gitignore
├── README.md
├── requirements.txt
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── unittests.yml
├── .vscode/
│   └── settings.json
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── data/
│   ├── benin_clean.csv
│   ├── benin-malanville.csv
│   ├── sierraleone_clean.csv
│   ├── sierraleone-bumbuna.csv
│   ├── togo_clean.csv
│   ├── togo-dapaong_qc.csv
│   ├── benin_plots/
│   ├── sierraleone_plots/
│   └── togo_plots/
├── notebooks/
│   ├── __init__.py
│   ├── benin_eda.ipynb
│   ├── compare_countries.ipynb
│   ├── README.md
│   ├── sierraleone_eda.ipynb
│   └── togo_eda.ipynb
├── scripts/
│   ├── __init__.py
│   └── README.md
├── src/
├── tests/
│   └── __init__.py
```

- **app/**: Streamlit dashboard code and utilities.
- **data/**: Raw and cleaned datasets, and plot output folders.
- **notebooks/**: Jupyter notebooks for EDA, cleaning, and comparison.
- **scripts/**: (Reserved) Python scripts for automation and data processing.
- **src/**: (Reserved) Source code for reusable modules and classes.
- **tests/**: (Reserved) Unit tests for code in `src/`.
- **.github/workflows/**: CI/CD workflow definitions.

---

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Abel5173/solar-challenge-week1.git
   cd solar-challenge-week1
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\activate    # Windows
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

---

## Usage

### Running Notebooks

1. Launch Jupyter:
   ```sh
   jupyter notebook
   ```
2. Open and run the notebooks in the `notebooks/` directory (e.g., `benin_eda.ipynb`, `sierraleone_eda.ipynb`, `togo_eda.ipynb`, `compare_countries.ipynb`).

### Running the Streamlit Dashboard

1. Ensure cleaned data files are present in the `data/` directory.
2. Run the dashboard:
   ```sh
   streamlit run app/main.py
   ```
3. Open the provided local URL in your browser.

#### Dashboard Features

- **Country Selector:** Choose which countries to compare.
- **Boxplots:** Visualize GHI distribution by country.
- **Top Regions Table:** See top regions by average GHI.
- **Modern UI:** Minimalist, glassmorphic, and cyberpunk-inspired design.
- **Responsive Layout:** Works on desktop and mobile.

### Running Tests

If/when tests are implemented in `tests/`:

```sh
pytest tests/
```

### Running CI Locally

You can check code style and run tests locally:

```sh
flake8 .
pytest
```

---

## CI/CD

- GitHub Actions workflows are defined in `.github/workflows/ci.yml` and `unittests.yml`.
- On each push or pull request, the workflow will:
  - Set up the Python environment
  - Install dependencies
  - Run linting and tests (if present)
  - Optionally, check notebook execution

---

## Contribution Guidelines

- Use feature branches for new work.
- Write clear, descriptive commit messages.
- Refactor repeated notebook code into functions or classes in `src/` for reusability.
- Add or update tests in `tests/` for new code.
- Ensure all code passes CI before submitting a Pull Request.

---

## License

This project is for educational purposes.

---

For questions or suggestions, please open an issue or contact the maintainer.
