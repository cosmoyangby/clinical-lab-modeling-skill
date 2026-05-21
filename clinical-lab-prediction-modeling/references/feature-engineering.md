# Feature Engineering

Use this guide to decide how to prepare clinical laboratory predictors before model fitting.

## 1. Classify Predictors

Separate predictors into:

- continuous laboratory indicators
- binary variables
- categorical variables
- ordinal variables
- repeated measurements
- derived ratios or scores
- time-dependent variables

Record unit, assay platform, reference interval, detection limit, and measurement timing.

## 2. Keep Clinical Time Order

Define:

- index time
- prediction window
- outcome window
- allowable look-back window

Do not use future measurements to predict past or baseline outcomes.

## 3. Handle Continuous Variables

For continuous lab indicators:

- inspect distribution, skewness, outliers, and impossible values
- consider log transform for strong right skew
- preserve continuous form when possible
- avoid arbitrary dichotomization
- use clinical cutoffs only when justified

If scaling is needed, fit scaling parameters on training data only.

## 4. Handle Nonlinearity

Check whether the effect is nonlinear.

Prefer:

- restricted cubic splines
- fractional polynomials
- clinically meaningful transforms

Use grouped categories mainly for description or sensitivity analysis, not as the default modeling form.

## 5. Handle Collinearity

Inspect:

- correlation matrix
- VIF
- biological overlap
- assay redundancy

When predictors are highly correlated, choose the variable set by:

- clinical interpretability
- measurement reliability
- availability
- cost
- biological plausibility

Avoid deleting variables mechanically.

## 6. Handle Derived Features

Use ratios, differences, indices, or scores only when clinically meaningful.

Rules:

- define formulas before modeling
- document units
- avoid creating many derived features when sample size is small
- use only information available at prediction time

## 7. Handle Repeated Measures

If multiple test results exist, choose one rule and pre-specify it:

- baseline value
- nearest value
- max or min value
- change from baseline
- slope
- time-weighted summary

For longitudinal prediction, consider landmark analysis or survival modeling.

## 8. Avoid Leakage

Keep the following inside the training or resampling pipeline:

- imputation
- scaling
- transformation selection
- feature selection
- cutoff optimization
- class rebalancing

Apply learned rules unchanged to validation and test data.

## 9. Choose Filtering Strategy

Use the data shape to choose the filtering method:

- strong clinical prior and few variables: keep the prespecified set
- many correlated predictors: use penalization or grouped selection
- many candidate markers and limited events: prefer stable penalized methods over univariable filtering
- mixed predictor types: keep clinically meaningful blocks

Avoid univariable P-value screening as the only filter.
