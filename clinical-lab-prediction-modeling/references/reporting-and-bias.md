# Reporting and Bias

Use this guide for study language, reporting structure, and quality checks.

Use TRIPOD/TRIPOD+AI for transparent reporting and PROBAST/PROBAST+AI for risk of bias and applicability checks.

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
- PROBAST for risk of bias and applicability
- PROBAST+AI when machine learning or AI models are involved
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
- intended use and decision context
- measurement timing and data leakage
- algorithm complexity relative to event count
- model transparency and availability for external validation

## 4. Check Applicability

Ask whether the model will still work in the intended setting.

Consider:

- platform differences
- assay differences
- prevalence shift
- center effects
- patient-mix shift
- timing differences
- treatment pathway differences
- missingness pattern differences
- outcome or reference standard differences

## 5. Demand Transparent Reporting

Require the final report to include:

- data source
- inclusion and exclusion criteria
- intended use and target population
- index or baseline time
- predictor definitions
- predictor measurement timing
- outcome definitions
- prediction horizon or reference standard
- preprocessing steps
- screening strategy
- model form
- validation strategy
- performance metrics
- calibration results
- clinical utility or decision-curve rationale when decisions are involved
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
- missing calibration
- unclear intended use
- unclear clinical use
