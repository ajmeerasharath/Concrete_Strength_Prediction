# AI 101 Mini-Project — Team Execution Plan

This document is our shared guide for building, testing and submitting the mini-project. It sets out what we are trying to do, how we will organise the work, and what we need to finish before submission.

Keep this file updated as the project develops. If anything here differs from the instructor's latest instructions or the official project brief, follow the official instructions.

---

## 1. Project overview

**Project title:** Predicting Concrete Compressive Strength Using Mix Ingredients and Curing Age

Concrete strength depends on the materials used in the mix and how long the concrete has been allowed to cure. In this project, we will use data from concrete samples to build a model that predicts compressive strength (MPa) from the mix ingredients and curing age.

- **Problem type:** Supervised learning — regression
- **Dataset:** [Concrete Compressive Strength Dataset on Kaggle](https://www.kaggle.com/datasets/elikplim/concrete-compressive-strength-data-set)
- **Number of records:** 1,030
- **Value we want to predict:** `concrete_compressive_strength` (MPa)

We will use these eight input features:

| Feature | Description |
|---|---|
| Cement | Cement quantity in the mix |
| Blast Furnace Slag | Blast furnace slag quantity |
| Fly Ash | Fly ash quantity |
| Water | Water quantity |
| Superplasticizer | Superplasticizer quantity |
| Coarse Aggregate | Coarse aggregate quantity |
| Fine Aggregate | Fine aggregate quantity |
| Age | Concrete curing age |

Our plan is to use all eight features for the main experiment.

## 2. What we are building

The aim is to create a simple, working prediction system. It should:

1. Read the dataset.
2. Check and prepare the data.
3. Separate the input features from the value we want to predict.
4. Split the data into training and testing sets.
5. Train a Multiple Linear Regression model.
6. Predict the strength of the test samples.
7. Evaluate the predictions using MAE, RMSE and R².
8. Allow someone to enter concrete mix details and get a predicted strength.

We will start with **Multiple Linear Regression** because it is straightforward to implement and explain. Once the basic version works, the team can decide whether there is enough time and a clear reason to compare it with another model.

## 3. Experiment setup and evaluation

For the main experiment, we plan to use:

- Training data: 80%
- Testing data: 20%
- `random_state=42`

Using a fixed random state makes it easier for the team to reproduce the same split.

We will report three evaluation metrics:

- **MAE:** The average absolute difference between actual and predicted strength. A lower value is better.
- **RMSE:** Measures prediction error while giving larger errors more weight. A lower value is better.
- **R²:** Shows how much of the variation in concrete strength is explained by the model. A value closer to 1 is generally better.

A previous run was reported with these results:

| Metric | Earlier result |
|---|---:|
| R² | 0.6276 |
| MAE | 7.7456 MPa |
| RMSE | 9.7965 MPa |

These are reference results, not guaranteed final results. We must run the finished code and use the values it actually produces. Do not hard-code these numbers into the program.

## 4. Project folder structure

We will keep the project organised so that each file has a clear job.

```text
concrete-strength-prediction/
│
├── data/
│   └── concrete_data.csv
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── model.py
│   ├── evaluation.py
│   └── main.py
│
├── results/
│   └── evaluation_results.txt
│
├── predict.py
├── requirements.txt
├── README.md
└── .gitignore
```

### What goes in each file?

| File | Purpose |
|---|---|
| `preprocessing.py` | Loads the CSV, checks the data, selects the features and target, and splits the dataset. |
| `model.py` | Creates and trains the regression model. |
| `evaluation.py` | Makes test predictions and calculates MAE, RMSE and R². |
| `main.py` | Runs the complete workflow. |
| `predict.py` | Takes mix details as input and displays a predicted strength. |
| `requirements.txt` | Lists the Python packages needed to run the project. |
| `README.md` | Explains the project and how to run it. |
| `results/` | Stores the results from the final experiment. |

The dataset filename must be the same in the code and documentation. Before adding the CSV to GitHub, check the course rules. If we decide not to upload the dataset, the README must explain where to download it and where to put it.

## 5. How to run the project

Open a terminal in the main project folder and install the required packages:

```bash
pip install -r requirements.txt
```

Then run the complete workflow:

```bash
python -m src.main
```

We need to test these commands before submission. If the final folder structure or entry point changes, update the instructions.

## 6. Team responsibilities

There are four people in the group. Each person should take responsibility for an agreed part of the work, but everyone should understand the overall project and be able to explain it.

Fill in the actual names and agreed responsibilities:

| Team member | Main responsibility |
|---|---|
| Member 1 | Execution Lead — coordinate implementation, integration and testing |
| Member 2 | Documentation / report |
| Member 3 | Presentation and video |
| Member 4 | Testing, results or another agreed deliverable |

This is only a starting point. Update the table to match the roles agreed by the team and the official course requirements.

### How we will work together

- Agree on the dataset, features, model and experiment before splitting up the work.
- Keep the code, report, slides and video consistent.
- Push work to GitHub regularly.
- Use commit messages that explain what changed.
- Each person should commit their own work so contributions are visible.
- Test the project after combining everyone's work.
- Do not call a task finished until the work is in the repository and has been checked.

## 7. Execution plan

### Step 1 — Set up GitHub

- Create the project repository.
- Add the folder structure shown above.
- Add a basic README and `.gitignore`.
- Make sure all team members have repository access.

### Step 2 — Prepare the dataset

- Download the dataset from Kaggle.
- Check the CSV filename and column names.
- Check for missing values and incorrect data types.
- Confirm the eight input features and target column.
- Put the CSV in the agreed location.

### Step 3 — Build the model

- Write the data preparation code.
- Split the dataset into training and testing sets.
- Train Multiple Linear Regression using the training data.
- Generate predictions for the test data.
- Keep the code organised in the files listed above.

### Step 4 — Evaluate and test

- Calculate MAE, RMSE and R².
- Check that the results are reasonable.
- Save the actual results in the `results/` folder.
- Test `predict.py` using a sample set of input values.
- Fix any errors before moving on.

### Step 5 — Finish the project materials

- Complete the README.
- Explain the dataset, features, model and results.
- Add clear setup and run instructions.
- Prepare the presentation and video according to the course brief.

### Step 6 — Check the final repository

- Test the project from a clean folder or environment.
- Follow the README instructions from start to finish.
- Check that the code does not depend on files stored only on one person's computer.
- Make sure all required files and links are present.
- Compare the repository with the official submission checklist.

## 8. Submission checklist

The course briefing says that the group should submit one GitHub repository containing the project work. The requirements captured from the briefing include:

- [ ] Working project code
- [ ] README and project documentation
- [ ] Final results
- [ ] Presentation with **exactly 5 slides**
- [ ] Project video of **no more than 5 minutes**
- [ ] Required disclosure of AI assistance or use
- [ ] Git commits that show each member's contribution
- [ ] Repository tested and ready to run

The mini-project contributes 20% of the lab marks. The briefing describes four deliverable areas worth 5 marks each. Check the original brief for the exact wording and marking criteria.

## 9. Suggested presentation outline

Keep the presentation to five slides:

1. **Problem and objective** — What we are predicting and why it matters.
2. **Dataset** — Dataset source, input features and target value.
3. **Method** — Train-test split and Multiple Linear Regression workflow.
4. **Results** — MAE, RMSE and R², with a short explanation.
5. **Conclusion** — What we achieved, the model's limitations and possible improvements.

## 10. Suggested video plan

The video must be no longer than five minutes. This is one possible structure:

| Time | Content |
|---|---|
| 0:00–0:30 | Introduce the project and its objective |
| 0:30–1:15 | Explain the dataset and input features |
| 1:15–2:15 | Explain the model and workflow |
| 2:15–3:30 | Run the project or demonstrate a prediction |
| 3:30–4:30 | Show and explain the evaluation results |
| 4:30–5:00 | Summarise the project and acknowledge team contributions |

## 11. Details to confirm as a team

Before submission, confirm the following from the original course brief and the team's final decisions:

- Names of all four members and their responsibilities.
- Exact description and marking criteria for each deliverable.
- Submission deadline and any repository naming rules.
- Whether the dataset CSV should be included in GitHub or downloaded separately.
- Required report format and video submission/link format.
- The exact AI-use disclosure required by the course.
- Whether we will submit only Multiple Linear Regression or include a comparison with another model.

---

## Immediate priority

Our first goal is to get the dataset loading, the regression model training and the evaluation working. Once that basic version runs correctly, we can test the prediction script and finish the README, presentation and video.

Getting a working version early will give us time to check everything together instead of trying to fix the whole project at the last minute.
