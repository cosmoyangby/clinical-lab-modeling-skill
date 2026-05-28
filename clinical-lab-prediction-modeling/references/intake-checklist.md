# Intake Checklist

Use this checklist before creating an analysis framework or downstream R agent prompt.

Do not create the full research decision framework until intake is complete, the uploaded dataset has been reviewed, or the user explicitly asks for a preliminary draft.

Use `bmj-methodology-anchor.md` when the user asks for a formal research framework, publication-oriented design, sample size judgment, validation plan, or reporting/bias review.

If core information is missing, return only:

1. known information
2. missing key information
3. focused follow-up questions
4. whether a dataset upload is needed
5. what can be provisionally assumed, if anything

## 1. Minimum Required Information

Ask for or infer:

- dataset path and file type
- study type
- intended clinical use
- target population and setting
- index or baseline time
- outcome variable
- prediction horizon or reference standard
- candidate predictors
- sample size
- number of events or positive cases
- validation structure

If these are missing, ask focused follow-up questions before designing the full workflow.

Core design information includes study type, intended use, target population, baseline or index time, outcome definition, prediction horizon or reference standard, event count, candidate predictors, and validation structure.

## 2. Study Type Questions

Clarify whether the project is:

- diagnostic
- prediction
- prognostic
- screening
- triage
- risk stratification

For diagnostic studies, ask:

- What is the target condition?
- What is the reference standard?
- Were predictors measured before or near diagnosis?
- Is the goal screening, diagnosis support, or triage?
- Are cases and controls sampled from the same intended-use population?
- Will the model output a probability, a cutoff result, or a triage category?

For prediction or prognostic studies, ask:

- What is the baseline time?
- What is the prediction horizon?
- What is the future outcome?
- Is there censoring or follow-up time?
- Will the output be used as absolute risk, risk category, or decision threshold?

## 3. Dataset Questions

Ask:

- Is the data cross-sectional, case-control, cohort, or nested case-control?
- Are there repeated measurements?
- Are there multiple centers, batches, platforms, or time periods?
- Is there a separate external validation dataset?
- Are train/test splits already defined?
- Are there platform, reagent, unit, or reference interval differences?
- Was any treatment started before predictor measurement?

## 4. Variable Questions

Ask:

- Which variables are laboratory indicators?
- Which variables are demographic or clinical covariates?
- Are units available?
- Are assay platforms available?
- Are reference intervals available?
- Are there derived ratios or scores?
- Are any variables measured after outcome or diagnosis?
- Are predictors available at the intended decision time in real clinical use?

## 5. Feasibility Questions

Ask:

- How many events or positive cases are available?
- How many candidate predictors are planned?
- How many candidate parameters may be created after dummy variables, splines, interactions, or derived features?
- What is the missingness pattern?
- Is class imbalance severe?
- Is external validation possible?
- Is the model intended for development only, external validation, or model updating?

If feasibility is weak, recommend a simpler and more exploratory analysis.

## 6. User Preference Questions

Ask whether the user prioritizes:

- interpretability
- prediction performance
- manuscript writing
- downstream R code generation
- external validation
- machine learning comparison

Use the answer to choose how much complexity to include.

## 7. When To Pause

Pause and ask the user before proceeding if:

- the outcome is unclear
- diagnostic versus prognostic framing is ambiguous
- predictors appear to be measured after the outcome
- validation structure is missing
- sample size or event count is unknown
- the requested model seems too complex for the data

Only proceed with a full preliminary draft despite missing information if the user explicitly asks for a draft based on current assumptions.
