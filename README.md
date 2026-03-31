# UVW College Enrollment Analytics

A data-driven analytics project using U.S. Census (UCI Adult) data to identify target audience segments for college enrollment and marketing strategy optimization.

---

## Overview

This project analyzes demographic and income patterns to help a hypothetical college identify individuals who are most likely to benefit from further education and career advancement programs.

The work is structured as a lightweight analytics pipeline, demonstrating how raw public data can be transformed into actionable insights for marketing and decision-making.

---

## Business Problem

A college aims to increase enrollment by targeting individuals who may benefit from upskilling, degree programs, or flexible education options.

This project focuses on the **$50K annual income threshold** and addresses:

* Which demographic factors are most associated with income level?
* Which population segments represent strong candidates for targeted outreach?
* How can these insights inform marketing strategy?

---

## Dataset

* Source: UCI Adult (Census Income) Dataset
* Files:

  * `adult.data`
  * `adult.names`

The dataset contains demographic and employment-related attributes such as:

* age
* education level
* occupation
* marital status
* work hours
* capital gain/loss

Target variable:

* income (`<=50K` or `>50K`)

---

## Project Structure

```
uvw-income-marketing-analytics/
├── README.md
├── requirements.txt
├── notebooks/
│   └── 01_income_analysis.ipynb
├── src/
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── analysis.py
│   ├── modeling.py
│   └── visualize.py
├── reports/
│   └── executive_summary.md
├── data/
└── figures/
```

---

## Key Questions Answered

* How does income vary across age groups?
* What is the relationship between education level and income?
* Which occupations are associated with higher income?
* How do work hours and capital gains relate to income?
* Which demographic segments are strong candidates for education-based outreach?

---

## Approach

### 1. Data Processing

* Loaded raw census data
* Standardized column names and formats
* Handled missing values (`?`)
* Prepared categorical and numerical features

---

### 2. Exploratory Analysis

* Age vs income distribution
* Education level vs income
* Occupation and demographic segmentation
* Work hours and capital gain patterns

---

### 3. Baseline Modeling

* Logistic regression pipeline
* One-hot encoding for categorical variables
* Missing value imputation
* Model evaluation (accuracy, precision, recall)

---

### 4. Business Insights

Key findings include:

* Individuals with lower education levels are significantly more likely to earn below $50K
* Income increases strongly with education level (Bachelor’s and above)
* Certain occupations and marital-status groups show higher income concentration
* Work hours alone are not a strong predictor of income; capital gain plays a role

---

## Marketing Recommendations

Based on the analysis:

* Target individuals earning below $50K with career advancement messaging
* Promote flexible learning options (online, part-time) for working adults
* Emphasize degree programs for individuals with high school or some college education
* Develop targeted campaigns based on occupation and education segments

---

## How to Run

### 1. Create environment

```
python -m venv .venv
source .venv/bin/activate
```

Windows:

```
.venv\Scripts\activate
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Run analysis

```
python -m src.analysis
```

---

### 4. Run modeling

```
python -m src.modeling
```

---

## Skills Demonstrated

* Data cleaning and preprocessing (Pandas)
* Exploratory data analysis and visualization
* Feature engineering and segmentation
* Basic machine learning (logistic regression)
* Translating data insights into business recommendations

---

## Future Improvements

* Add model interpretability (feature importance / SHAP)
* Compare multiple models (Random Forest, XGBoost)
* Build a simple dashboard (Streamlit)
* Automate data pipeline and reporting

---

## Notes

This project is designed to demonstrate how data analysis can support real-world decision-making, particularly in marketing and user segmentation scenarios.
