# Manuscript Methods Template

Use this guide to draft the statistical methods section for a clinical laboratory model study.

When producing a deliverable, write the methods draft in both Chinese and English unless the user requests one language only.

## 1. Study Type Statement

Start by naming the model type precisely.

Diagnostic wording:

```text
We developed and evaluated a diagnostic model to estimate the probability of [target condition] using clinical laboratory indicators measured at [index time]. The reference standard was [reference standard].
```

Prediction or prognostic wording:

```text
We developed and evaluated a prediction model to estimate the risk of [future outcome] within [prediction horizon] among [target population] at [baseline time].
```

## 2. Dataset and Participants

Describe:

- data source
- study period
- inclusion criteria
- exclusion criteria
- sample size
- number of events or positive cases
- validation cohort if available

## 3. Predictor and Outcome Definitions

State:

- outcome definition
- predictor measurement timing
- laboratory platforms or assay methods
- units and reference intervals when relevant
- handling of repeated measurements

## 4. Missing Data and Preprocessing

Describe:

- missingness inspection
- imputation strategy
- transformation
- scaling
- outlier handling
- leakage prevention

Keep all preprocessing fit within the training data or resampling process.

## 5. Feature Engineering and Predictor Selection

Describe:

- prespecified clinical predictors
- derived indicators or ratios
- nonlinearity assessment
- collinearity assessment
- predictor selection strategy
- how selection was nested within validation

Avoid writing that variables were selected only by univariable P values.

## 6. Model Development

Describe candidate models and rationale.

Possible wording:

```text
A logistic regression model was used as the baseline model. Penalized regression and machine learning models were considered when supported by sample size, class balance, and validation design.
```

For survival outcomes, replace logistic regression with Cox or survival modeling language.

## 7. Validation

Describe:

- training and validation split
- bootstrap or cross-validation
- external validation if available
- hyperparameter tuning
- optimism correction when used

Clearly separate apparent, internally validated, test-set, and external validation performance.

## 8. Performance Metrics

For diagnostic models, report:

- AUC
- sensitivity
- specificity
- PPV
- NPV
- LR+
- LR-
- threshold strategy

For prediction/prognostic models, report:

- C-statistic or AUC
- calibration plot
- calibration intercept
- calibration slope
- Brier score
- decision curve analysis

## 9. Software

Report software and packages.

Example:

```text
All analyses were performed using R version [version]. Data processing and modeling used [packages]. Statistical tests were two-sided when applicable.
```

## 10. Limitations Language

Add method-specific limitations:

- limited sample size
- limited event count
- lack of external validation
- single-center data
- assay platform differences
- risk of overfitting
- limited clinical implementation evidence
