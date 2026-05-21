# Sample Size

Use this guide to judge whether a clinical lab prediction study is feasible.

## 1. Check Basic Feasibility

Collect:

- total sample size
- number of events or positive cases
- number of non-events or negative cases
- candidate predictor count
- missingness proportion
- expected validation set size
- number of centers or batches

## 2. Do Not Overuse EPV

Do not rely only on EPV >= 10.

Use a broader feasibility check:

- expected model complexity
- candidate parameter count
- outcome prevalence
- anticipated shrinkage
- overfitting risk
- external validation needs

## 3. Match Sample Size to Model Type

If sample size is small:

- keep predictor count low
- avoid many interaction terms
- avoid many derived features
- prefer penalized or simple regression

If sample size is moderate:

- use clinical pre-specification
- allow limited feature selection
- use internal validation

If sample size is large:

- compare candidate model families
- still keep leakage control and external validation

## 4. Count Events, Not Just Rows

For binary or time-to-event outcomes, the number of events matters more than row count alone.

Check:

- events per candidate parameter
- minority class size
- censoring burden
- outcome prevalence

## 5. Plan Validation Early

Reserve enough data for:

- internal validation
- threshold tuning
- external validation if available

Do not spend the full dataset on model building and then try to validate later.

## 6. Use Development and Validation Guides

Use BMJ-style sample size and validation guidance as the methodological anchor.

For development planning, consider `pmsampsize` in R when the inputs are available.

## 7. Report Limits Clearly

If the study is underpowered for a complex model, say so directly and simplify the design.

Report the consequences:

- unstable coefficients
- wide confidence intervals
- limited generalizability
- higher overfitting risk
