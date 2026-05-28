# Sample Size

Use this guide to judge whether a clinical lab prediction study is feasible.

Use BMJ 2020 sample size guidance as the anchor. Do not reduce feasibility to EPV >= 10.

## 1. Check Basic Feasibility

Collect:

- total sample size
- number of events or positive cases
- number of non-events or negative cases
- candidate predictor count
- candidate parameter count after dummy coding, nonlinear terms, interactions, and derived features
- missingness proportion
- expected validation set size
- number of centers or batches
- anticipated outcome prevalence
- anticipated model performance if known

## 2. Do Not Overuse EPV

Do not rely only on EPV >= 10.

Use a broader feasibility check:

- expected model complexity
- candidate parameter count
- outcome prevalence
- anticipated shrinkage
- overfitting risk
- expected optimism in apparent performance
- precision of overall outcome risk estimate
- precision of calibration slope or calibration-in-the-large when relevant
- external validation needs

## 3. Match Sample Size to Model Type

If sample size is small:

- keep predictor count low
- avoid many interaction terms
- avoid many derived features
- prefer penalized or simple regression
- avoid broad machine learning comparisons

If sample size is moderate:

- use clinical pre-specification
- allow limited feature selection
- use internal validation

If sample size is large:

- compare candidate model families
- still keep leakage control and external validation
- still report calibration and clinical utility

## 4. Count Events, Not Just Rows

For binary or time-to-event outcomes, the number of events matters more than row count alone.

Check:

- events per candidate parameter
- minority class size
- censoring burden
- outcome prevalence
- number of parameters consumed by categorical levels and splines

## 5. Plan Validation Early

Reserve enough data for:

- internal validation
- threshold tuning
- external validation if available

Do not spend the full dataset on model building and then try to validate later.

For small datasets, prefer resampling-based internal validation over a single random split that leaves too few events in either development or test data.

## 6. Use Development and Validation Guides

Use BMJ-style sample size and validation guidance as the methodological anchor.

For development planning, consider `pmsampsize` in R when the inputs are available.

For external validation planning, consider whether the validation sample is large enough to estimate calibration, discrimination, and clinical utility with useful precision.

## 7. Feasibility Labels

Use one of these labels in the deliverable:

- 适合模型开发：events and candidate parameters plausibly support the planned model.
- 适合简化模型开发：development is possible but model complexity should be constrained.
- 适合探索性建模：results may inform future work but are not clinically ready.
- 更适合关联分析：data do not support a reliable prediction model.
- 需要补充数据或外部验证：development or transportability claims require additional data.

## 8. Report Limits Clearly

If the study is underpowered for a complex model, say so directly and simplify the design.

Report the consequences:

- unstable coefficients
- wide confidence intervals
- limited generalizability
- higher overfitting risk
