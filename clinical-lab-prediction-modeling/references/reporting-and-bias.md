# Reporting and Bias

Use this guide for study language, reporting structure, and quality checks.

## 1. Separate Diagnostic and Prognostic Language

Diagnostic studies ask whether a condition is present now.

Use terms such as:

- reference standard
- index test
- diagnostic accuracy
- sensitivity
- specificity
- likelihood ratio
- cutoff

Prediction or prognostic studies ask about future risk.

Use terms such as:

- prediction horizon
- absolute risk
- baseline time
- follow-up
- calibration
- clinical utility

Do not mix these terms casually.

## 2. Use Reporting Frameworks

Anchor the manuscript in:

- TRIPOD
- TRIPOD+AI when machine learning is involved
- BMJ prediction-model development and validation guidance

## 3. Check Bias Domains

Review:

- participant selection
- predictor definition
- outcome definition
- missing data
- sample size
- model development
- validation
- calibration
- clinical utility
- reproducibility

## 4. Check Applicability

Ask whether the model will still work in the intended setting.

Consider:

- platform differences
- assay differences
- prevalence shift
- center effects
- patient-mix shift
- timing differences

## 5. Demand Transparent Reporting

Require the final report to include:

- data source
- inclusion and exclusion criteria
- predictor definitions
- outcome definitions
- preprocessing steps
- screening strategy
- model form
- validation strategy
- performance metrics
- calibration results
- limitations
- code availability

## 6. Keep the Conclusion Narrow

Do not overclaim.

State whether the model:

- is diagnostic or prognostic
- is internally validated only or externally validated
- is ready for clinical use or still exploratory
- is limited by sample size, bias, or data shift

## 7. Review Before Release

Before handing off output, check for:

- data leakage
- incorrect language
- unsupported cutoff claims
- missing validation
- overinterpretation of AUC
- unclear clinical use
