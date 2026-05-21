# Do and Do Not

Use this file as a final guardrail before producing advice or deliverables.

## Do

- Define the model type before discussing methods.
- Ask focused questions when outcome, predictors, validation, or intended use are unclear.
- Keep diagnostic, prediction, and prognostic language separate.
- Match feature engineering and model choice to sample size, event count, missingness, class balance, and validation design.
- Treat logistic or Cox regression as an interpretable baseline.
- Use machine learning only when data volume, validation, and interpretability needs support it.
- Report discrimination, calibration, threshold performance, and clinical utility when relevant.
- Keep preprocessing, feature selection, tuning, and threshold optimization inside training or resampling.
- State whether results are exploratory, internally validated, externally validated, or ready for further implementation study.

## Do Not

- Do not provide patient-specific diagnosis or treatment advice.
- Do not mix diagnostic accuracy language with prognostic risk language.
- Do not use univariable P values as the only predictor selection rule.
- Do not dichotomize continuous laboratory indicators without clinical justification.
- Do not use validation or external data for feature selection, tuning, or cutoff optimization.
- Do not present machine learning as automatically superior.
- Do not rely on AUC alone.
- Do not claim clinical readiness without adequate validation and applicability assessment.
- Do not turn project-specific code structure, audit tables, or local file paths into general skill rules.
