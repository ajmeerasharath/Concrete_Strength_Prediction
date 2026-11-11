# Concrete Strength Prediction using Linear Regression

Predicts the compressive strength of concrete (in MPa) from its mix ingredients and age, using multiple linear regression in Python (pandas, NumPy, scikit-learn, Matplotlib).

**AI101: Data Science and AI Essentials with Python · School of AI & Data Engineering, IIT Ropar**

---

## Table of contents

1. [Team and roles](#team-and-roles)
2. [About the project](#about-the-project)
3. [Dataset](#dataset)
4. [Project structure](#project-structure)
5. [How the project works](#how-the-project-works)
6. [Setup](#setup)
7. [How to run](#how-to-run)
8. [Expected output](#expected-output)
9. [Results](#results)
10. [Troubleshooting](#troubleshooting)
11. [Slides and video](#slides-and-video)
12. [AI-use disclosure](#ai-use-disclosure)

---

## Team and roles

| Member | Entry no. | GitHub | Role |
|---|---|---|---|
| Ajmeera Sharath | 2026MCB1507 | [ajmeerasharath](https://github.com/ajmeerasharath) | Documentation lead |
| Kabir Jhamb | 2026AIB1045 | [Kabir-Jhamb](https://github.com/kabir-jhamb) | Execution lead |
| Amit Patel | 2026EEB1319 | [Amitpatel99-coder](https://github.com/Amitpatel99-coder) | PPT lead |
| Bhargav Sugat Shende | 2026EEB1335 | [bhargavshende](https://github.com/bhargavshende) | Video lead |

All four members contributed code (see the commit history).

---

## About the project

Concrete is the most widely used construction material, and its compressive strength is normally measured by crushing test samples after curing. This is slow, because the standard test is done at 28 days. This project asks: **can we predict strength directly from the mix recipe and the age of the sample?**

The target is a continuous number (strength in MPa), so this is a **regression** problem. We use **multiple linear regression** as a transparent baseline: every feature gets a coefficient we can read and interpret.

---

## Dataset

- **File:** `data/concrete_data.csv`
- **Source:** Concrete Compressive Strength dataset (I-Cheng Yeh), from the UCI Machine Learning Repository. Kaggle copy: https://www.kaggle.com/datasets/elikplim/concrete-compressive-strength-data-set
- **Size:** 1,030 rows and 9 columns, with no missing values (25 duplicate rows are kept)
- **Target:** `concrete_compressive_strength` (MPa)

| Column | Description | Unit |
|---|---|---|
| `cement` | Cement in the mix | kg/m³ |
| `blast_furnace_slag` | Blast furnace slag | kg/m³ |
| `fly_ash` | Fly ash | kg/m³ |
| `water` | Water | kg/m³ |
| `superplasticizer` | Superplasticizer | kg/m³ |
| `coarse_aggregate` | Coarse aggregate | kg/m³ |
| `fine_aggregate` | Fine aggregate | kg/m³ |
| `age` | Age of the sample | days |
| `concrete_compressive_strength` | **Target:** compressive strength | MPa |

---

## Project structure

```text
concrete_strength_prediction_linear_regression_/
├── Code/
│   ├── main.py             # runs the whole pipeline in order
│   ├── analysis.py         # loads the CSV, prints summaries, saves the correlation heatmap
│   ├── preprocessing.py    # train/test split + median imputation
│   ├── training.py         # trains the linear regression, saves actual-vs-predicted plot
│   └── evaluation.py       # R², MAE, MSE, RMSE, residual plot
├── data/
│   ├── README.md
│   └── concrete_data.csv   # dataset (included, so no download step is needed)
├── PPT (5).pdf             # project slides
├── results/                # tables and graph which will be shown on running the code
├── outputs/                # created automatically when the code runs (tables + graphs)
├── run_all.py              # one-command setup and run script
├── requirements.txt        # pinned Python packages
├── .gitignore
└── README.md
```

## How the project works

**Dataset → Data cleaning → Train/test split → Linear regression → Prediction → Evaluation**

1. **Load and inspect** (`analysis.py`): reads the CSV, cleans the column names, checks shape, data types, missing values and duplicates, and prints mean, median and standard deviation. It also saves the covariance matrix, the correlation matrix and a correlation heatmap.
2. **Preprocess** (`preprocessing.py`): separates the 8 features from the target, splits the data **80% train / 20% test** (`random_state=42`), and fits a median imputer on the training data only, so no information leaks from the test set.
3. **Train** (`training.py`): fits scikit-learn's `LinearRegression`, prints the intercept and each feature coefficient, and saves an actual-vs-predicted plot.
4. **Evaluate** (`evaluation.py`): reports R², MAE, MSE and RMSE for both training and test sets, saves the metrics table and a residual plot, and prints a short written analysis (including an overfitting check).

---

## Setup

**Requirements**

- **Python.** 
- An internet connection for the first run (to install packages)
- Git

Packages (pinned in `requirements.txt`): `numpy`, `pandas`, `matplotlib`, `scikit-learn`.

---

## How to run

### Option 1 (recommended): one command

`run_all.py` finds a compatible Python, creates a virtual environment (`.venv`), installs `requirements.txt`, and runs the whole pipeline.

**Windows (PowerShell):**

```powershell
git clone https://github.com/ajmeerasharath/concrete_strength_prediction_linear_regression_.git
cd concrete_strength_prediction_linear_regression_
python run_all.py
```

**Linux / macOS:**

```bash
git clone https://github.com/ajmeerasharath/concrete_strength_prediction_linear_regression_.git
cd concrete_strength_prediction_linear_regression_
python3 run_all.py
```

Graphs are saved to `outputs/` without opening pop-up windows. To also see the graph windows while it runs, add `--show`:

```bash
python run_all.py --show
```

### Option 2: manual steps

**Windows (PowerShell):**

```powershell
git clone https://github.com/ajmeerasharath/concrete_strength_prediction_linear_regression_.git
cd concrete_strength_prediction_linear_regression_
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python Code\main.py
```

**Linux / macOS:**

```bash
git clone https://github.com/ajmeerasharath/concrete_strength_prediction_linear_regression_.git
cd concrete_strength_prediction_linear_regression_
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python Code/main.py
```

When running manually, three graph windows open one after another. Close each window to let the script continue. Windows can also be skipped by setting `MPLBACKEND=Agg` before running (Linux/macOS: `MPLBACKEND=Agg python Code/main.py`).

The script uses relative paths only, so it can be run from any computer after cloning.

---

## Expected output

The terminal prints these sections in order: loading the dataset, dataset overview, descriptive statistics, covariance and correlation matrices, preprocessing, training (intercept and coefficients), evaluation, and a final success message. A successful run ends like this:

```text
========== MODEL EVALUATION ==========
              R2     MAE       MSE     RMSE
Training  0.6105  8.3301  110.6449  10.5188
Testing   0.6276  7.7456   95.9709   9.7965

========== PROJECT COMPLETED SUCCESSFULLY ==========
Project: Concrete Compressive Strength Prediction
Algorithm: Multiple Linear Regression
```

**Files created in `outputs/`:**

| File | Contents |
|---|---|
| `descriptive_statistics.csv` | Mean, median and standard deviation of every column |
| `covariance_matrix.csv` | Covariance matrix |
| `correlation_matrix.csv` | Correlation matrix |
| `correlation_heatmap.png` | Heatmap of the correlation matrix |
| `actual_vs_predicted.png` | Test-set predictions against true values |
| `evaluation_metrics.csv` | R², MAE, MSE, RMSE for training and testing |
| `residual_plot.png` | Residuals on the test set |

---

## Results

**Metrics** (80/20 split, `random_state=42`):

| Set | R² | MAE (MPa) | MSE | RMSE (MPa) |
|---|---|---|---|---|
| Training | 0.6105 | 8.3301 | 110.6449 | 10.5188 |
| Testing | **0.6276** | **7.7456** | 95.9709 | **9.7965** |

**Learned coefficients** (change in predicted strength in MPa for a one-unit increase, other features fixed; intercept = −28.82):

| Feature | Coefficient |
|---|---|
| `superplasticizer` | +0.3106 |
| `water` | −0.1353 |
| `cement` | +0.1190 |
| `age` | +0.1164 |
| `blast_furnace_slag` | +0.1085 |
| `fly_ash` | +0.0822 |
| `fine_aggregate` | +0.0241 |
| `coarse_aggregate` | +0.0179 |


**What the results show**

- The model explains about **63%** of the variation in test-set strength. Predictions are off by roughly **7.7 MPa** on average (MAE).
- Training and test R² are close (0.61 vs 0.63), so there is no sign of overfitting. The model is more likely **underfitting**, because the relationship between ingredients and strength is not perfectly linear (for example, strength rises quickly with age at first, then levels off).
- Cement, superplasticizer and age are associated with higher strength, and more water is associated with lower strength. These are associations in this dataset, not proof of cause and effect.
- Possible improvements: add non-linear or interaction features, try polynomial regression, random forest or gradient boosting, and use cross-validation.

---

## Troubleshooting

- **`No compatible Python was found`:** install 64-bit Python 3.12 from python.org (on Windows, tick *py launcher*), then run `run_all.py` again.
- **`python` is not recognized (Windows):** try `py run_all.py`.
- **Package installation fails:** check your internet connection, turn off any VPN, and run the command again. If it still fails, delete the `.venv` folder and retry.
- **PowerShell blocks activating the environment:** run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then activate again.
- **`Dataset not found`:** run the script from inside the cloned folder, and check that `data/concrete_data.csv` exists.
- **`can't open file ... Code/main.py` on Linux/macOS:** the folder must be named `Code` with a capital C.
- **The script seems stuck (manual run):** a graph window is open. Close it and the script continues.
- **`destination path ... already exists` when cloning:** you already have a copy. Run `cd` into it and `git pull`, or clone into a different folder name.


## AI-use disclosure

- **ChatGPT:** helped with project planning, understanding Python and machine learning concepts, the linear regression implementation, and debugging suggestions.
- **Claude:** helped draft and structure this README and run_all.py . The documentation lead edited it, and the team checked every command and number against an actual run of the code.
- **How we checked it:** we ran the code ourselves, compared the printed metrics with the numbers in this README, and tested the setup steps on a fresh clone.
- **Dataset and results:** no AI was used to generate the dataset or the results. All numbers come from running the code in this repository.

Every team member understands the code and can explain any part of it.
