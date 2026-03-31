# UVW College Enrollment Analytics

A business-focused analytics project built on the UCI Adult (Census Income) dataset to identify audience segments relevant to college enrollment and career-advancement marketing.

---

## Overview

This project analyzes demographic, education, and employment patterns to understand which population segments are more strongly associated with income level. The analysis is framed around a practical marketing use case: helping a college identify groups that may benefit from degree programs, certificate programs, or flexible upskilling options.

The repository is structured as a lightweight analytics project rather than a single notebook. It includes reusable data-loading and preprocessing modules, exploratory analysis, visualization scripts, and a baseline classification model.

---

## Business Problem

A college wants to improve enrollment by targeting individuals who may benefit from further education, career transition support, or skill-based programs.

This project uses the **$50K annual income threshold** as a simple segmentation target and asks:

* Which demographic and employment features are most associated with income level?
* Which education and occupation segments are most relevant for outreach?
* How can these findings inform marketing strategy for adult learners?

---

## Dataset

* Source: [UCI Adult (Census Income) Dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/)
* Files used:

  * [`adult.data`](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data)
  * [`adult.names`](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names)

The dataset includes demographic and employment-related attributes such as:

* age
* workclass
* education
* marital status
* occupation
* relationship
* race
* sex
* capital gain / loss
* hours worked per week
* native country

Target variable:

* income (`<=50K` or `>50K`)

---

## Project Structure

```text
uvw-income-marketing-analytics/
├── README.md
├── requirements.txt
├── notebooks/
│   └── 01_income_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── analysis.py
│   ├── modeling.py
│   └── visualize.py
├── data/
│   ├── README.md
│   ├── raw/
│   │   └── adult.data
│   └── processed/
├── Reports
│   └── executive_summary.md
└── figures/
```

---

## Key Questions Answered

* How does high-income share change across age groups?
* How does education level relate to income outcomes?
* Which occupation groups show stronger high-income concentration?
* Which segments are most relevant for education-focused outreach?
* Can a simple baseline model classify income level from demographic and employment features?

---

## Approach

### 1. Data Loading and Cleaning

* Load raw Adult dataset from a local file
* Apply descriptive column names
* Standardize whitespace in string fields
* Convert `?` values to missing values
* Normalize target labels for consistent analysis

### 2. Exploratory Analysis

* Age and income relationship
* Education-level income patterns
* Segment summaries for business interpretation
* Additional notebook-based analysis for occupation, work hours, and demographic patterns

### 3. Visualization

* Save reusable charts into `figures/`
* Focus on decision-oriented plots such as:

  * high-income rate by age
  * high-income rate by education
  * occupation-level income patterns

### 4. Baseline Modeling

* Logistic regression pipeline
* ColumnTransformer-based preprocessing
* Median imputation for numeric features
* Most-frequent imputation + one-hot encoding for categorical features
* Evaluation using accuracy, ROC AUC, and classification report

---

## Selected Insights

Examples of patterns explored in this project include:

* Higher education levels are associated with substantially higher rates of income above $50K
* Lower education groups are more concentrated below the $50K threshold
* Some occupation segments show meaningfully different income outcomes
* Age and work profile help contextualize which adult-learner groups may respond to different program offerings

---

## Marketing Recommendations

Based on the analysis, example outreach directions include:

* Promote certificate-first or career-advancement messaging to lower-income working adults
* Highlight flexible formats such as online or part-time programs for employed learners
* Target outreach by education level, especially for individuals with high school or some college backgrounds
* Tailor messaging by occupation cluster where upskilling or credentialing may have clearer value

---

## How to Run

### 1. Create and activate an environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the dataset

Download `adult.data` from the UCI repository and place it in:

```text
data/raw/adult.data
```

### 4. Run the analysis script

```bash
python -m src.analysis
```

This script prints basic dataset checks, generates a business-facing segment preview, and saves charts to `figures/`.

### 5. Run the baseline model

```bash
python -m src.modeling
```

This script trains a logistic regression baseline and prints evaluation metrics.

### 6. Open the notebook

```text
notebooks/01_income_analysis.ipynb
```

The notebook contains exploratory analysis, visual outputs, and additional narrative interpretation.

---

## Skills Demonstrated

* Data loading and preprocessing with Pandas
* Missing-value handling and target normalization
* Modular Python project organization
* Exploratory data analysis and data visualization
* Audience segmentation thinking for business use cases
* Baseline machine learning with scikit-learn pipelines

---

## Future Improvements

* Add model interpretability for clearer feature-level explanation
* Compare logistic regression against tree-based models
* Expand segmentation outputs beyond education into occupation and age-band groups
* Build a simple dashboard for marketer-facing exploration
* Add automated tests for preprocessing and loading utilities

---

## Notes

This project is intended as a portfolio-style example of how public demographic data can be turned into structured analysis, reusable Python modules, and decision-oriented outputs for a marketing use case.






