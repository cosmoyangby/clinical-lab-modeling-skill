# Predictor Selection

Use this guide to choose candidate predictors and variable selection strategies for clinical laboratory model studies.

Variable selection must serve the clinical question. It should not be a mechanical search for the smallest P values or highest AUC.

## 1. Build the Candidate Predictor Pool

Classify predictors before any modeling:

- core clinical variables: age, sex, severity, major comorbidities, treatment context
- primary laboratory indicators: the main markers related to the study question
- adjustment variables: confounders or baseline clinical factors
- exploratory laboratory indicators: secondary or hypothesis-generating markers
- derived features: ratios, scores, changes, slopes, or grouped indices
- unavailable or unsafe predictors: variables measured after outcome, diagnosis, treatment decision, or reference standard

Exclude variables before modeling when they are:

- unavailable at the intended decision time
- direct consequences of the outcome
- components of the outcome or reference standard
- identifiers, administrative artifacts, or post-treatment information
- too sparse or poorly measured to support reliable use

Do not exclude a clinically important predictor only because its univariable P value is not significant.

## 2. Count Parameters, Not Only Variables

Estimate candidate parameter count before choosing a selection method.

Remember that parameters can come from:

- categorical variable levels
- spline terms
- interactions
- derived ratios
- repeated-measurement summaries
- dummy variables for center, batch, platform, or assay type

If candidate parameters are too many relative to events, reduce complexity before comparing models.

## 3. Recommended Selection Routes

Choose one main route and state why.

### Prespecified Full Model

Use when:

- predictors are few
- clinical prior knowledge is strong
- sample size and event count are adequate
- interpretability matters

Why:

- avoids data-driven instability
- preserves clinical meaning
- works well for confirmatory or publication-oriented models

Not suitable when:

- candidate predictors are many
- predictors are highly correlated
- event count cannot support all parameters

### Clinical Preselection Plus Shrinkage

Use when:

- predictors are clinically selected but overfitting risk remains
- sample size is modest
- the goal is a stable, interpretable model

Possible methods:

- ridge regression
- penalized logistic or Cox regression
- global shrinkage after model fitting

Why:

- keeps clinically important variables
- reduces coefficient instability

### Penalized Selection

Use when:

- predictors are many
- laboratory indicators are correlated
- event count is limited relative to candidate parameters
- a parsimonious model is needed

Possible methods:

- LASSO
- elastic net
- adaptive LASSO when justified

Why:

- combines selection and shrinkage
- handles correlated predictor sets better than simple P-value filtering

Notes:

- elastic net is often preferable to LASSO when laboratory indicators cluster biologically.
- choose tuning parameters inside cross-validation or bootstrap, not on final validation data.

### Stability-Based Selection

Use when:

- variable selection results may be unstable
- multiple correlated laboratory markers compete
- robustness is more important than choosing a single lucky subset

Possible methods:

- bootstrap selection frequency
- repeated cross-validation selection frequency
- stability selection with penalized models

Report:

- selected variables
- selection frequency or stability evidence
- whether clinically essential variables were forced in

### Block-Wise Selection

Use when predictors form clinically meaningful groups:

- demographics
- baseline severity
- routine laboratory tests
- immune cell subsets
- inflammatory markers
- microbiology or molecular tests

Why:

- compares incremental value of predictor groups
- fits clinical reasoning better than isolated marker hunting

Use with:

- likelihood ratio tests for nested regression models
- cross-validated performance change
- calibration and clinical utility checks

### Machine Learning Feature Selection

Use only when:

- sample size is adequate
- event count supports complexity
- validation is strong
- the goal includes exploration or model comparison

Possible methods:

- recursive feature elimination
- tree-based importance
- Boruta
- regularized gradient boosting

Limits:

- variable importance does not equal causal or clinical importance
- importance rankings can be unstable with correlated laboratory indicators
- feature selection must be nested inside resampling

## 4. Methods To Avoid as Main Strategy

Avoid as the main variable selection strategy:

- selecting predictors only by univariable P value
- automatic stepwise regression without validation
- choosing variables only because they maximize apparent AUC
- deleting correlated variables mechanically by correlation cutoff alone
- selecting cutoffs before validation
- selecting variables after looking at external validation performance

Allowed limited uses:

- univariable summaries for description
- stepwise regression as sensitivity analysis, clearly labeled
- correlation screening to identify redundancy before clinical review
- exploratory ML importance to generate hypotheses

## 5. Collinearity Strategy

When laboratory indicators are correlated:

1. identify correlation clusters
2. check biological meaning and measurement reliability
3. choose one representative marker when clinical meaning is similar
4. use ridge or elastic net when several correlated markers may jointly contribute
5. avoid reporting multiple redundant markers as independent discoveries

Do not remove variables only because VIF is high without considering clinical meaning.

## 6. Nonlinearity and Selection

Do not force continuous predictors into binary categories for easy selection.

For key continuous laboratory indicators:

- inspect nonlinear relationships
- consider restricted cubic splines or fractional polynomials
- count spline degrees of freedom as parameters
- keep nonlinear modeling inside the development process

If sample size is limited, prefer simpler transformations over many flexible terms.

## 7. Missingness and Selection

Before selecting predictors, classify missingness:

- structurally missing
- clinically informative missing
- random or likely random missing
- platform or center-related missing

Rules:

- do not select variables only because they have complete data
- do not drop clinically important variables solely for moderate missingness
- avoid complete-case selection unless missingness is minimal and defensible
- perform imputation inside resampling when model performance is estimated

If missingness itself is clinically meaningful, consider a missingness indicator only with explicit justification.

## 8. Small Sample or Low Event Count

If events are limited:

- reduce candidate parameter count before modeling
- force only essential clinical variables
- avoid broad laboratory panels
- avoid many derived ratios
- avoid complex ML feature selection
- prefer penalization, shrinkage, or exploratory framing

If event count is very low, recommend association analysis or feasibility analysis rather than a full prediction model.

## 9. Reporting Requirements

The final framework should state:

- initial candidate predictor pool
- variables excluded before modeling and why
- selected main predictor selection route
- variables forced in for clinical reasons
- variables selected by data-driven methods
- how tuning or selection was validated
- whether selection was internal-only or externally evaluated
- sensitivity analyses if selection is uncertain

Use cautious language when selection is unstable or exploratory.
