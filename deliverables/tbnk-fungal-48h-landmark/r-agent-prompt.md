# R Agent Prompt: TBNK 48h Landmark Fungal Infection Prediction

You are an R analysis agent.

Task:
Build a clinical laboratory indicator-based 48-hour landmark prediction model analysis for ICU patients, using TBNK and early clinical variables to predict 14-day pulmonary fungal PCR positivity.

Study boundary:
- Diagnostic vs prediction/prognostic: prediction model, not diagnostic accuracy study.
- Intended use: early ICU risk stratification.
- Target population and setting: ICU patients eligible at 48 hours after ICU admission.
- Baseline or index time: 48 hours after ICU admission.
- Outcome: pulmonary fungal PCR positivity within 14 days after the 48-hour landmark.
- Prediction horizon or reference standard: 14-day future risk; PCR is performed after clinical suspicion, so verification bias must be reported.

Data:
- File path: [fill in dataset path]
- File type: [csv / xlsx / other]
- Sample size: approximately 300
- Events or positive cases: approximately 45
- Candidate predictors: age, sex, CD3, CD4, CD8, NK cells, B cells, CD4/CD8 ratio, antimicrobial exposure within 48h, mechanical ventilation within 48h, and other variables confirmed available before the landmark.
- Candidate parameter concerns: correlated TBNK indicators, CD4/CD8 derived ratio, categorical clinical variables, possible nonlinear continuous effects.
- Validation structure: internal validation only; prefer bootstrap validation.
- Independent validation data: none.

Required steps:
1. Inspect variables, missingness, and class balance.
2. Confirm that every predictor is available before or at the 48-hour landmark.
3. Exclude or flag patients with pulmonary fungal PCR positivity before the 48-hour landmark.
4. Build the 14-day outcome after the landmark and document handling of death, discharge, no PCR testing, and outcome NA.
5. Apply leakage-safe preprocessing inside the training or resampling pipeline.
6. Check TBNK units, implausible values, assay/platform fields if available, and correlation among TBNK indicators.
7. Use age and sex as core clinical predictors unless the study team specifies otherwise.
8. Evaluate a baseline clinical model and a clinical + TBNK model.
9. Use parsimonious logistic regression or penalized logistic regression as the main modeling route.
10. Consider ridge or elastic net for correlated TBNK indicators and limited event count.
11. Treat random forest, XGBoost, or other machine learning models as exploratory only unless sample size and validation strength are clearly adequate.
12. Validate internally with bootstrap or repeated cross-validation.
13. Report discrimination, calibration, prediction error, threshold performance, and clinical utility.

Required outputs:
- cleaned analysis dataset
- missingness and class balance summary
- predictor timing and leakage check summary
- TBNK correlation summary
- candidate predictor table
- model summary table
- performance table
- calibration figure
- ROC curve and PR curve
- decision curve when clinically meaningful thresholds are specified
- threshold-specific risk stratification table
- sensitivity analysis for death/discharge/outcome NA handling if feasible
- final model object
- concise analysis log

Code rules:
- Use clear, reproducible R code.
- Add `#` comments before major code blocks.
- Keep preprocessing, imputation, scaling, feature selection, and tuning inside resampling.
- Do not leak validation data into tuning.
- Do not select predictors, thresholds, transformations, or model family using final validation performance.
- Distinguish apparent performance from internally validated performance.
- Save outputs with explicit file names.

Recommended packages:
- tidyverse
- readxl
- janitor
- naniar
- mice
- glmnet
- rms
- pROC
- PRROC or yardstick
- rsample
- caret or tidymodels
- rmda or dcurves
- broom
- flextable or gt

Important cautions:
- PCR testing is clinically triggered, so the modeled outcome may represent clinically suspected and PCR-confirmed infection rather than systematic infection incidence.
- Death and discharge before outcome assessment should not be silently dropped; document the primary coding rule and run sensitivity analysis if possible.
- With approximately 45 events, avoid high-dimensional feature engineering and complex machine learning as the main conclusion.
- No external validation is available, so do not claim clinical readiness.
