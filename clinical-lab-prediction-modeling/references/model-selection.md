# Model Selection

Use this guide to choose candidate models and screening strategies for clinical lab studies.

## 1. Start With the Research Type

- diagnostic model: current disease or state
- prediction model: future outcome risk
- prognostic model: risk after a defined baseline condition
- screening or triage model: who needs more testing

Use diagnostic language for current-state classification and prediction language for future risk.

## 2. Start Simple

Use logistic regression as the default baseline for binary outcomes.

Use Cox regression or related survival models for time-to-event outcomes.

Prefer interpretable models first when:

- sample size is modest
- event count is limited
- validation is weak
- clinical explanation matters

## 3. Decide Screening Strategy

Use `predictor-selection.md` for the full variable selection methodology.

Choose predictor screening based on data characteristics:

- no screening: when variables are few and clinically justified
- expert pre-specification: when prior knowledge is strong
- clinical preselection plus shrinkage: when interpretability matters but overfitting risk remains
- penalized selection: when predictors are many or correlated
- stability-based selection: when robustness matters
- block-wise selection: when predictors belong to clear clinical groups
- machine learning feature selection: only when data volume and validation are strong

Avoid one-round univariable P-value selection as the main rule.

## 4. Handle Machine Learning Carefully

Consider machine learning only when:

- sample size is adequate
- class balance is acceptable or can be handled properly
- events are sufficient for model complexity
- validation design is strong
- interpretability tradeoff is acceptable

Possible candidates:

- random forest
- XGBoost
- LightGBM
- SVM
- Naive Bayes
- kNN

Use these only when they match the problem better than a simpler model.

## 5. Compare Models Fairly

Compare candidate models with the same:

- split strategy
- preprocessing pipeline
- resampling scheme
- metric set

Do not tune on validation or test data.

## 6. Choose Metrics by Goal

For diagnostic models, focus on:

- sensitivity
- specificity
- PPV
- NPV
- likelihood ratios

For prediction/prognostic models, focus on:

- discrimination
- calibration
- Brier score
- decision curve analysis

If classes are imbalanced, add PR-AUC and threshold-specific metrics.

## 7. Prefer Validation-Aware Selection

Use nested CV, bootstrap, or separate validation data when tuning many candidates.

Do not let feature selection and hyperparameter tuning leak across folds.

## 8. Use This Decision Logic

- few predictors, strong prior: logistic or Cox
- many correlated predictors: penalized regression
- nonlinear signal, larger data: spline-augmented regression or tree-based methods
- enough data and strong validation: machine learning comparison
- high explainability need: parsimonious regression
