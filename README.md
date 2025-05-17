# Solar Challenge Week 1

A project for learning Git, CI/CD, and exploratory data analysis (EDA) on solar and meteorological datasets from West Africa.

## Project Overview

This repository contains data analysis workflows and scripts for exploring and cleaning solar resource and weather data from Benin, Togo, and Sierra Leone. The goal is to demonstrate best practices in code organization, reproducibility, and collaborative development using Git and CI/CD.

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
├── data/
│   ├── benin_clean.csv
│   ├── benin-malanville.csv
│   ├── sierraleone-bumbuna.csv
│   ├── togo_clean.csv
│   └── togo-dapaong_qc.csv
├── notebooks/
│   ├── __init__.py
│   ├── benin_eda.ipynb
│   ├── README.md
│   └── togo_eda.ipynb
├── scripts/
│   ├── __init__.py
│   └── README.md
├── src/
├── tests/
│   └── __init__.py
```

- **data/**: Raw and cleaned datasets.
- **notebooks/**: Jupyter notebooks for EDA and visualization.
- **scripts/**: (Planned) Python scripts for automation and data processing.
- **src/**: (Planned) Source code for reusable modules and classes.
- **tests/**: (Planned) Unit tests for code in `src/`.
- **.github/workflows/**: CI/CD workflow definitions.

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

## Usage

### Running Notebooks

1. Launch Jupyter:
   ```sh
   jupyter notebook
   ```
2. Open and run the notebooks in the `notebooks/` directory (e.g., `benin_eda.ipynb`).

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

## Contribution Guidelines

- Use feature branches for new work.
- Write clear commit messages.
- Refactor repeated notebook code into functions or classes in `src/` for reusability.
- Add or update tests in `tests/` for new code.
- Ensure all code passes CI before submitting a Pull Request.

## License

This project is for educational purposes.

---

For questions or suggestions, please open an issue or contact the maintainer.
