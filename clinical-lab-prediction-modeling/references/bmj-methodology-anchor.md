# BMJ Methodology Anchor

Use this file as the scientific anchor for clinical laboratory indicator-based prediction, prognostic, and diagnostic model research.

Primary references:

- BMJ 2024 step-by-step clinical prediction model development guide: https://www.bmj.com/content/386/bmj-2023-078276
- BMJ 2024 model evaluation series, part 1: https://www.bmj.com/content/384/bmj-2023-074819
- BMJ 2024 external validation guidance, part 2: https://www.bmj.com/content/384/bmj-2023-074820
- BMJ 2024 external validation sample size guidance, part 3: https://www.bmj.com/content/384/bmj-2023-074821
- BMJ 2020 sample size for clinical prediction model development: https://www.bmj.com/content/368/bmj.m441
- TRIPOD+AI 2024 reporting guideline: https://www.bmj.com/content/385/bmj-2023-078378
- PROBAST+AI 2025 risk of bias and applicability tool: https://www.bmj.com/content/388/bmj-2024-082505

## Core Principles

1. Start from clinical use, not algorithm choice.
2. Define the target population, clinical setting, intended use, outcome, prediction horizon or reference standard before modeling.
3. Select candidate predictors from clinical relevance, availability at the intended decision time, measurement quality, and prior evidence.
4. Treat sample size as a design problem, not a post-hoc limitation. Do not rely only on EPV >= 10.
5. Avoid arbitrary dichotomization of continuous laboratory indicators.
6. Model nonlinearity when clinically plausible and sample size permits.
7. Handle missing data explicitly; do not default to complete-case analysis without justification.
8. Keep all preprocessing, imputation, predictor selection, threshold selection, and hyperparameter tuning inside the development or resampling workflow.
9. Separate apparent, internal validation, test-set, and external validation performance.
10. Report calibration and clinical utility whenever risk prediction is intended to support decisions.
11. Do not claim clinical readiness without appropriate external validation and clear intended-use evidence.
12. Use TRIPOD+AI for transparent reporting and PROBAST+AI for bias/applicability checks.

## BMJ-Style Development Sequence

Use this sequence when designing the research framework:

1. Specify intended use and decision context.
2. Define target population and data source.
3. Define outcome and time horizon or reference standard.
4. Define candidate predictors and measurement timing.
5. Assess sample size, events, candidate parameter count, and expected overfitting risk.
6. Plan missing data handling before model fitting.
7. Plan predictor transformations, nonlinear terms, and clinically justified interactions.
8. Choose model family and predictor selection strategy.
9. Develop the model with leakage-safe preprocessing.
10. Estimate optimism and internal validity.
11. Evaluate discrimination, calibration, prediction error, thresholds, and clinical utility.
12. Validate externally when an independent setting, time period, platform, or population exists.
13. Report transparently, including limitations, applicability, and whether the model remains exploratory.

## Development Versus Evaluation

Development answers:

- Can a model be built for this intended use?
- Which predictors and model form are appropriate?
- What is the internally validated performance?

External validation answers:

- Does a locked model transport to a different but relevant setting?
- Does performance change because of population, prevalence, assay platform, center, time, or care-process differences?

Do not mix development and external validation data.

## External Validation Readiness

Before external validation, the model must have:

- locked predictor definitions
- locked preprocessing
- locked model equation or model object
- locked threshold or risk categories, if used
- no feature selection, tuning, or recalibration using the external data unless clearly labeled as model updating

## Clinical Laboratory Specific Checks

For laboratory indicators, always check:

- specimen timing relative to baseline and outcome
- assay platform and unit consistency
- reference interval differences
- batch, center, or machine effects
- clinically implausible values
- derived ratios or scores
- whether any predictor is measured after diagnosis, treatment, or outcome

These checks are especially important because laboratory variables can easily encode timing, treatment, or disease confirmation leakage.
