## Data

This project uses the **UCI Adult (Census Income) dataset**, a widely used public dataset for income classification and demographic analysis.

### Source

* UCI Repository: https://archive.ics.uci.edu/ml/machine-learning-databases/adult/
* Dataset file: https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
* Attribute description: https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names

---

### Recommended Local Layout

```text
data/
├── README.md
├── raw/
│   └── adult.data
└── processed/
```

---

### Setup

Download the dataset from the UCI repository and place it in:

```text
data/raw/adult.data
```

The project will handle preprocessing and generate cleaned datasets as needed.

---

### Schema

Columns expected by the project:

* age
* workclass
* fnlwgt
* education
* education-num
* marital-status
* occupation
* relationship
* race
* sex
* capital-gain
* capital-loss
* hours-per-week
* native-country
* income
