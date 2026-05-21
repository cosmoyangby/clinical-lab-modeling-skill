# Machine Learning Suitability

Use this guide to decide whether machine learning models are appropriate for a clinical lab study.

## 1. Do Not Assume Superiority

Machine learning is not automatically better than regression.

Use machine learning only when the data and study goal justify it.

## 2. Check Data Readiness

Before using machine learning, assess:

- total sample size
- event or positive-case count
- candidate predictor count
- class imbalance
- missingness
- external validation availability
- measurement platform consistency
- interpretability requirement

If these are weak, prefer simpler and more interpretable models.

## 3. Suitable Situations

Machine learning may be reasonable when:

- sample size is adequate
- predictor relationships are likely nonlinear
- interactions are plausible
- predictors are numerous
- validation design is strong
- model interpretability can be addressed

Candidate models include:

- random forest
- XGBoost
- LightGBM
- SVM
- Naive Bayes
- kNN

Neural networks require especially cautious justification.

## 4. Unsuitable Situations

Avoid complex machine learning when:

- events are few
- classes are severely imbalanced
- external validation is absent
- predictors are few and clinically clear
- missingness is high and poorly understood
- the model must be highly explainable
- the analysis is mainly exploratory

## 5. Class Imbalance

For imbalanced data, consider:

- stratified splitting
- class weights
- threshold-specific metrics
- PR-AUC
- sensitivity at fixed specificity
- specificity at fixed sensitivity

Use SMOTE or synthetic sampling only inside training resampling.

## 6. Fair Comparison

Compare regression and machine learning models with the same:

- train/test split
- preprocessing pipeline
- resampling scheme
- performance metrics
- validation data

Do not tune models on the test set or external validation cohort.

## 7. Interpretability

When machine learning is used, provide interpretation support:

- variable importance
- partial dependence or accumulated local effects
- SHAP-style explanations when available
- clinically meaningful explanation of important predictors

Do not treat explanation plots as causal evidence.

## 8. Minimum Reporting

Report:

- candidate models
- tuning strategy
- resampling design
- preprocessing pipeline
- class imbalance handling
- discrimination
- calibration
- clinical utility
- final model rationale
