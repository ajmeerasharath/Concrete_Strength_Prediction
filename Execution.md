# Execution Guide

## 1. Project Structure

The project uses the following directory structure:

```text
concrete_strength_prediction_linear_regression/
│
├── data/
│   ├── README.md
│   └── concrete_data.csv
│
├── code/
│   ├── main.py
│   ├── preprocessing.py
│   ├── analysis.py
│   ├── training.py
│   └── evaluation.py
│
├── requirements.txt
├── README.md
├── Execution.md
└── .gitignore
```

## 2. Requirements

- Python 3.x (use a version compatible with the pinned packages).
- Required libraries are listed in `requirements.txt`.
- Dataset: `data/concrete_data.csv`.

## 3. Environment Setup

Open a terminal in the project root directory.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## 4. Execute the Project

Run the main program from the project root:

```bash
python code/main.py
```

The main script coordinates the project workflow:

1. Dataset loading and preprocessing.
2. Exploratory data analysis.
3. Linear Regression model training.
4. Model evaluation and prediction.

Each module handles its respective task.

## 5. Execution Verification

Before considering execution complete, verify that:

- All required Python files are present.
- The dataset exists at `data/concrete_data.csv`.
- All dependencies install successfully.
- The main script executes without errors.
- Training and evaluation complete successfully.
- Actual evaluation results are generated.

## 6. Fresh Clone Test

To verify reproducibility, clone the repository into a new location:

```bash
git clone https://github.com/ajmeerasharath/concrete_strength_prediction_linear_regression_.git
```

Navigate into the repository:

```bash
cd concrete_strength_prediction_linear_regression_
```

Repeat the environment setup, dependency installation and execution steps.

The project should run using only the instructions provided in this guide.

---

**Execution Lead:** Kabir Jhamb

**Responsibility:** Environment setup, dependency management, project integration and execution testing.
