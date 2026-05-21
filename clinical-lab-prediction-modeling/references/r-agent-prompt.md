# R Agent Prompt

Use this template to hand off a standardized analysis request to an R agent after key methodological choices are confirmed.

If study type, outcome definition, predictor pool, or validation structure is unresolved, label the prompt as a draft and keep placeholders explicit.

For formal delivery, save the prompt as a standalone Markdown file. Keep it executable for another agent without requiring that agent to read the full research decision Word document.

## Prompt Template

```text
You are an R analysis agent.

Task:
Build a clinical laboratory indicator-based [diagnostic / prediction / prognostic] model analysis for the dataset below.

Study boundary:
- Diagnostic vs prediction/prognostic: [state clearly]
- Outcome: [name and definition]
- Prediction horizon or reference standard: [specify]
- Intended use: [screening / diagnosis / risk prediction / triage / stratification]

Data:
- File path: [path]
- File type: [csv / xlsx / other]
- Sample size: [n]
- Events or positive cases: [n]
- Candidate predictors: [list]
- Validation structure: [train/test / internal CV / external validation]
- Independent validation data: [none / external-center / platform-based / other]

Required steps:
1. Inspect variables, missingness, and class balance.
2. Apply leakage-safe preprocessing inside the training pipeline.
3. Check collinearity and nonlinear relationships.
4. Choose an analysis strategy based on data characteristics.
5. Compare a baseline regression model with optional machine learning models only if appropriate.
6. Validate internally and externally if possible.
7. Report discrimination, calibration, threshold performance, and clinical utility.
8. If external validation data are provided, use them only after the model is locked.

Required outputs:
- cleaned analysis dataset
- model summary table
- performance table
- calibration figure
- ROC or PR curve when appropriate
- decision curve when appropriate
- threshold-specific diagnostic or risk-stratification table
- final model object
- concise analysis log

Code rules:
- Use clear, reproducible R code.
- Add `#` comments before major code blocks.
- Keep preprocessing inside resampling.
- Do not leak validation data into tuning.
- Save outputs with explicit file names.

Packages:
[list the packages needed for this dataset and model]
```

## Usage Notes

- Fill the template with dataset-specific details before sending it downstream.
- Keep the prompt short when the analysis is simple.
- Add survival-analysis instructions when the outcome is time-to-event.
- Add separate validation instructions when an external cohort exists.
